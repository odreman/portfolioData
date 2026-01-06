# Generación Multimodal de Contenido

## Descripción

Aplicación completa para generación multimodal de contenido que integra tres tipos de salida: texto, audio e imágenes. Incluye una API REST construida con FastAPI y una interfaz web interactiva con Streamlit para facilitar el uso y la experimentación.

## Características

### Generación de Texto
- Modelo: TinyLlama-1.1B-Chat-v1.0
- Respuestas conversacionales y contenido creativo
- Control de temperatura para ajustar creatividad

### Generación de Audio
- Modelo: Bark (suno/bark-small)
- Múltiples voces disponibles
- Salida en formato WAV

### Generación de Imágenes
- Modelo: Tiny-SD (segmind/tiny-sd)
- Generación a partir de descripciones textuales
- Salida en formato PNG

### Modo Inteligente
- Detección automática del tipo de contenido solicitado
- Respuestas combinadas según el contexto
- Procesamiento optimizado de prompts

## Estructura del Proyecto

```
├── main.py              # API FastAPI
├── models.py            # Carga y configuración de modelos
├── schemas.py           # Esquemas de datos
├── utils.py             # Utilidades de procesamiento
├── client.py            # Interfaz Streamlit
└── requirements.txt     # Dependencias
```

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar la API:
```bash
python main.py
```

4. En otra terminal, ejecutar la interfaz:
```bash
streamlit run client.py
```

## Uso

### API Endpoints

- `GET /` - Información general
- `GET /generate/text` - Generación de texto
- `GET /generate/audio` - Generación de audio
- `GET /generate/image` - Generación de imágenes
- `GET /generate/smart` - Modo inteligente
- `GET /health` - Estado del sistema

### Interfaz Web

Acceder a `http://localhost:8501` para usar la interfaz gráfica que incluye:
- Selección de modo de generación
- Configuración de parámetros
- Historial de conversaciones
- Estadísticas de uso

## Parámetros

### Texto
- `prompt`: Texto de entrada
- `temperature`: Nivel de creatividad (0.1 - 1.0)

### Audio
- `prompt`: Texto a convertir
- `preset`: Voz seleccionada (v2/en_speaker_1 a v2/en_speaker_9)

### Imagen
- `prompt`: Descripción de la imagen

## Configuración

Los modelos se cargan automáticamente al primer uso. La aplicación detecta automáticamente si hay GPU disponible para acelerar el procesamiento.

## Requisitos del Sistema

- Python 3.8+
- 4GB RAM mínimo (8GB recomendado)
- GPU opcional (mejora rendimiento)

## Dependencias Principales

- FastAPI
- Streamlit
- Transformers
- Diffusers
- Torch
- Soundfile