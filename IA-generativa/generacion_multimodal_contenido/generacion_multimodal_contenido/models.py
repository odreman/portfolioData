# models.py
import torch
import numpy as np
from transformers import AutoProcessor, AutoModel, pipeline, Pipeline
from diffusers import DiffusionPipeline
from PIL import Image
from schemas import VoicePresets

# Configuración del dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Dispositivo: {device}")

# Variables globales para cache de modelos
text_model = None
audio_processor = None
audio_model = None
image_model = None

# Configuración del sistema
SYSTEM_PROMPT = """Eres un asistente que responde en español de forma clara y directa. 
Ayudas con recetas, poemas, explicaciones y tareas creativas."""

def load_text_model() -> Pipeline:
    """Carga el modelo de generación de texto"""
    global text_model
    if text_model is None:
        print("Cargando modelo de texto...")
        text_model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
            device=device,
        )
        print("Modelo de texto cargado")
    return text_model

def generate_text(pipe: Pipeline, prompt: str, temperature: float = 0.7) -> str:
    """Genera texto usando el modelo cargado"""
    
    contextualized_prompt = improve_prompt(prompt)
    formatted_prompt = f"<|system|>\n{SYSTEM_PROMPT}<|user|>\n{contextualized_prompt}<|assistant|>\n"
    
    try:
        predictions = pipe(
            formatted_prompt,
            temperature=temperature,
            max_new_tokens=200,
            do_sample=True,
            top_k=40,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=pipe.tokenizer.eos_token_id,
            return_full_text=False
        )
        
        output = predictions[0]["generated_text"]
        cleaned_output = clean_output(output)
        
        return cleaned_output
        
    except Exception as e:
        print(f"Error en generación: {e}")
        return f"No se pudo generar una respuesta para: {prompt}"

def improve_prompt(prompt: str) -> str:
    """Mejora el prompt según el contexto"""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ["poema", "poem", "verso"]):
        return f"Escribe un poema sobre: {prompt.replace('poema', '').strip()}"
    elif any(word in prompt_lower for word in ["receta", "recipe", "pastel", "cake", "cocinar"]):
        return f"Proporciona una receta para: {prompt}"
    elif any(word in prompt_lower for word in ["explica", "explain", "qué es"]):
        return f"Explica: {prompt}"
    elif any(word in prompt_lower for word in ["ayuda", "help", "cómo"]):
        return f"Ayuda con: {prompt}"
    else:
        return prompt

def clean_output(output: str) -> str:
    """Procesa y limpia la salida del modelo"""
    
    # Remover tokens del modelo
    tokens_to_remove = [
        "<|system|>", "<|user|>", "<|assistant|>", "</s>", "<s>",
        "Assistant:", "User:", "System:"
    ]
    
    for token in tokens_to_remove:
        output = output.replace(token, "")
    
    # Limpiar formato
    lines = [line.strip() for line in output.split('\n') if line.strip()]
    result = '\n'.join(lines).strip()
    
    # Validaciones
    if len(result) < 10:
        return "No se pudo generar una respuesta completa."
    
    # Formato básico
    if result and not result[0].isupper():
        result = result[0].upper() + result[1:]
    
    if not result.endswith(('.', '!', '?')):
        result += '.'
    
    return result

def load_audio_model() -> tuple[AutoProcessor, AutoModel]:
    """Carga el modelo de audio"""
    global audio_processor, audio_model
    if audio_processor is None or audio_model is None:
        print("Cargando modelo de audio...")
        audio_processor = AutoProcessor.from_pretrained("suno/bark-small")
        audio_model = AutoModel.from_pretrained("suno/bark-small")
        audio_model = audio_model.to(device)
        print("Modelo de audio cargado")
    return audio_processor, audio_model

def generate_audio(
    processor: AutoProcessor,
    model: AutoModel,
    prompt: str,
    preset: VoicePresets,
) -> tuple[np.array, int]:
    """Genera audio desde texto"""
    try:
        if len(prompt) > 100:
            prompt = prompt[:100]
        
        inputs = processor(text=[prompt], return_tensors="pt", voice_preset=preset)
        
        with torch.no_grad():
            output = model.generate(**inputs, do_sample=True)
        
        output = output.cpu().numpy().squeeze()
        sample_rate = model.generation_config.sample_rate
        return output, sample_rate
        
    except Exception as e:
        print(f"Error en audio: {e}")
        # Fallback a silencio
        sample_rate = 24000
        silence = np.zeros(int(sample_rate * 1.0), dtype=np.float32)
        return silence, sample_rate

def load_image_model() -> DiffusionPipeline:
    """Carga el modelo de generación de imágenes"""
    global image_model
    if image_model is None:
        print("Cargando modelo de imágenes...")
        image_model = DiffusionPipeline.from_pretrained(
            "segmind/tiny-sd", 
            torch_dtype=torch.float32, 
            device=device,
            use_safetensors=False,
            safety_checker=None,
            requires_safety_checker=False
        )
        print("Modelo de imágenes cargado")
    return image_model

def generate_image(pipe: DiffusionPipeline, prompt: str) -> Image.Image:
    """Genera imagen desde prompt"""
    with torch.no_grad():
        output = pipe(
            prompt, 
            num_inference_steps=10,
            guidance_scale=7.5,
            width=512,
            height=512
        ).images[0]
    return output