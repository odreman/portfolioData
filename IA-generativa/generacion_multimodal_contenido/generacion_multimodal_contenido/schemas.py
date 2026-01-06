# schemas.py
from typing import Literal
from pydantic import BaseModel
from enum import Enum

# Tipos de contenido que puede generar la aplicación
class ContentType(str, Enum):
    TEXT = "text"
    AUDIO = "audio"
    IMAGE = "image"

# Presets de voz disponibles para la generación de audio
VoicePresets = Literal[
    "v2/en_speaker_1", 
    "v2/en_speaker_2", 
    "v2/en_speaker_3", 
    "v2/en_speaker_4", 
    "v2/en_speaker_5",
    "v2/en_speaker_6",
    "v2/en_speaker_7", 
    "v2/en_speaker_8", 
    "v2/en_speaker_9"
]

class GenerationRequest(BaseModel):
    prompt: str
    content_type: ContentType
    voice_preset: VoicePresets = "v2/en_speaker_1"
    temperature: float = 0.7

class GenerationResponse(BaseModel):
    success: bool
    message: str
    content_type: ContentType