# utils.py
from typing import Literal
from PIL import Image
from io import BytesIO
import soundfile
import numpy as np
import re

def img_to_bytes(image: Image.Image, img_format: Literal["PNG", "JPEG"] = "PNG") -> bytes:
    """Convierte imagen PIL a bytes"""
    buffer = BytesIO()
    image.save(buffer, format=img_format)
    return buffer.getvalue()

def audio_array_to_buffer(audio_array: np.array, sample_rate: int) -> BytesIO:
    """Convierte array de audio a buffer"""
    buffer = BytesIO()
    soundfile.write(buffer, audio_array, sample_rate, format="wav")
    buffer.seek(0)
    return buffer

def detect_content_intent(prompt: str) -> str:
    """Detecta el tipo de contenido solicitado"""
    prompt_lower = prompt.lower()
    
    # Palabras clave para imágenes
    image_keywords = ["imagen", "image", "foto", "picture", "dibujo", "drawing", "mostrar", "visual"]
    if any(keyword in prompt_lower for keyword in image_keywords):
        return "image"
    
    # Palabras clave para audio
    audio_keywords = ["di ", "say ", "habla", "speak", "audio", "voz", "pronuncia"]
    if any(keyword in prompt_lower for keyword in audio_keywords):
        return "audio"
    
    return "text"

def clean_prompt_for_image(prompt: str) -> str:
    """Limpia prompt para generación de imágenes"""
    words_to_remove = ["imagen de", "photo of", "mostrar", "show"]
    cleaned = prompt.lower()
    
    for word in words_to_remove:
        cleaned = cleaned.replace(word, "")
    
    return cleaned.strip()

def clean_prompt_for_audio(prompt: str) -> str:
    """Limpia prompt para generación de audio"""
    commands = ["di ", "say ", "habla ", "speak "]
    cleaned = prompt
    
    for cmd in commands:
        cleaned = cleaned.replace(cmd, "")
    
    if len(cleaned) > 100:
        cleaned = cleaned[:100]
    
    return cleaned.strip()