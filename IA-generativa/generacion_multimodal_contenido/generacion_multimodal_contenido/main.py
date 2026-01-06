# main.py
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import Response, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import traceback

from models import (
    load_text_model, generate_text,
    load_audio_model, generate_audio,
    load_image_model, generate_image
)
from schemas import ContentType, VoicePresets, GenerationRequest
from utils import (
    img_to_bytes, audio_array_to_buffer, 
    detect_content_intent, clean_prompt_for_image, clean_prompt_for_audio
)

app = FastAPI(
    title="Integrated AI Content Generator",
    description="API para generación de contenido multimodal",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Endpoint principal"""
    return {
        "message": "Integrated AI Content Generator API",
        "endpoints": {
            "text": "/generate/text",
            "audio": "/generate/audio", 
            "image": "/generate/image",
            "smart": "/generate/smart"
        }
    }

@app.get("/generate/text")
def generate_text_endpoint(
    prompt: str = Query(..., description="Texto del prompt"),
    temperature: float = Query(0.7, ge=0.1, le=1.0, description="Temperatura de generación")
) -> str:
    """Genera texto basado en el prompt"""
    try:
        pipe = load_text_model()
        output = generate_text(pipe, prompt, temperature)
        return output
    except Exception as e:
        print(f"Error en generación de texto: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Error generando texto: {str(e)}")

@app.get(
    "/generate/audio",
    responses={status.HTTP_200_OK: {"content": {"audio/wav": {}}}},
    response_class=StreamingResponse,
)
def generate_audio_endpoint(
    prompt: str = Query(..., description="Texto para convertir a audio"),
    preset: VoicePresets = Query("v2/en_speaker_1", description="Preset de voz")
):
    """Genera audio a partir de texto"""
    try:
        print(f"Iniciando generación de audio para: '{prompt}'")
        processor, model = load_audio_model()
        cleaned_prompt = clean_prompt_for_audio(prompt)
        print(f"Prompt procesado: '{cleaned_prompt}'")
        
        output, sample_rate = generate_audio(processor, model, cleaned_prompt, preset)
        
        return StreamingResponse(
            audio_array_to_buffer(output, sample_rate), 
            media_type="audio/wav"
        )
    except Exception as e:
        print(f"Error en generación de audio: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Error generando audio: {str(e)}")

@app.get(
    "/generate/image",
    responses={status.HTTP_200_OK: {"content": {"image/png": {}}}},
    response_class=Response,
)
def generate_image_endpoint(
    prompt: str = Query(..., description="Descripción de la imagen")
):
    """Genera imagen basada en el prompt"""
    try:
        pipe = load_image_model()
        cleaned_prompt = clean_prompt_for_image(prompt)
        output = generate_image(pipe, cleaned_prompt)
        return Response(content=img_to_bytes(output), media_type="image/png")
    except Exception as e:
        print(f"Error en generación de imagen: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Error generando imagen: {str(e)}")

@app.get("/generate/smart")
def generate_smart_endpoint(
    prompt: str = Query(..., description="Prompt para procesamiento inteligente"),
    force_type: Optional[ContentType] = Query(None, description="Forzar tipo de contenido"),
    voice_preset: VoicePresets = Query("v2/en_speaker_1", description="Preset de voz"),
    temperature: float = Query(0.7, ge=0.1, le=1.0, description="Temperatura de generación")
):
    """Endpoint inteligente que detecta automáticamente el tipo de contenido"""
    try:
        print(f"Procesamiento inteligente para: '{prompt}'")
        
        if force_type:
            content_type = force_type.value
        else:
            content_type = detect_content_intent(prompt)
        
        print(f"Tipo detectado: {content_type}")
        
        # Generar respuesta de texto
        text_pipe = load_text_model()
        text_response = generate_text(text_pipe, prompt, temperature)
        
        response_data = {
            "text_response": text_response,
            "detected_type": content_type,
            "original_prompt": prompt
        }
        
        # Generar contenido adicional según tipo
        if content_type == "image":
            try:
                image_pipe = load_image_model()
                cleaned_prompt = clean_prompt_for_image(prompt)
                image_output = generate_image(image_pipe, cleaned_prompt)
                response_data["image_prompt"] = cleaned_prompt
                response_data["message"] = "Imagen generada. Usa /generate/image para obtenerla."
            except Exception as e:
                response_data["image_error"] = str(e)
                print(f"Error en imagen: {e}")
                
        elif content_type == "audio":
            try:
                audio_processor, audio_model = load_audio_model()
                cleaned_prompt = clean_prompt_for_audio(prompt)
                audio_output, sample_rate = generate_audio(audio_processor, audio_model, cleaned_prompt, voice_preset)
                response_data["audio_prompt"] = cleaned_prompt
                response_data["message"] = "Audio generado. Usa /generate/audio para obtenerlo."
            except Exception as e:
                response_data["audio_error"] = str(e)
                print(f"Error en audio: {e}")
        
        return response_data
        
    except Exception as e:
        print(f"Error en generación inteligente: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Error en generación inteligente: {str(e)}")

@app.get("/health")
def health_check():
    """Endpoint de estado"""
    return {"status": "healthy", "message": "API funcionando correctamente"}

if __name__ == "__main__":
    import uvicorn
    print("Iniciando AI Content Generator API...")
    print("Los modelos se cargarán bajo demanda")
    print("API disponible en: http://localhost:8000")
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info",
        access_log=True
    )