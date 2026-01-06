# Transcripción de Audio con Whisper y Clasificación Zero-Shot

## 📋 Descripción

Este proyecto demuestra cómo construir aplicaciones web con modelos Transformer para procesamiento del lenguaje natural, específicamente para transcripción de audio y clasificación de texto zero-shot.

## 🎯 Objetivo

Construir aplicaciones web interactivas utilizando modelos Transformer para:
1. Transcripción de audio multilingüe con Whisper
2. Clasificación de texto zero-shot sin necesidad de entrenamiento previo
3. Combinación de ambas técnicas en un clasificador de audios zero-shot

## 📊 Contenido del Proyecto

El proyecto incluye:
- **Ejemplo I**: Interfaz de usuario para transcripción de audio con Gradio
- **Ejemplo II**: Clasificación de texto zero-shot con modelos Transformer
- **Demo completa**: Clasificador de audios zero-shot que combina transcripción y clasificación

## 🛠️ Tecnologías Utilizadas

- **Transformers (Hugging Face)** - Modelos pre-entrenados de NLP
- **Gradio** - Construcción de interfaces web interactivas
- **Faster-Whisper** - Transcripción de audio multilingüe optimizada
- **PyTorch** - Framework de deep learning
- **OpenAI Whisper** - Modelo de transcripción de audio

## 📖 Temas Cubiertos

- Transcripción de audio con Whisper
- Clasificación zero-shot con modelos Transformer (BART, DeBERTa)
- Construcción de interfaces web con Gradio
- Pipeline de procesamiento de audio y texto
- Aplicaciones interactivas de NLP
- Prompt engineering para clasificación zero-shot

## 📁 Estructura del Proyecto

```
transcripcion_audio_whisper/
├── README.md
└── transcripcion_audio_whisper.ipynb
```

## 🚀 Ejecución

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install transformers gradio faster-whisper sentencepiece torch
```

2. **Importante**: Para que las demostraciones se ejecuten rápidamente, se recomienda usar una GPU. Activa la GPU en tu entorno (Colab, Jupyter, etc.) antes de ejecutar las celdas.

3. Abre el notebook `transcripcion_audio_whisper.ipynb` en Jupyter

4. Ejecuta todas las celdas para ver las demostraciones completas

## 📈 Resultados Clave

- Interfaz interactiva para transcripción de audio multilingüe
- Sistema de clasificación zero-shot que funciona con múltiples idiomas
- Demo completa de clasificador de audios que combina transcripción y clasificación
- Aplicación práctica de modelos Transformer en problemas reales

## 💡 Características Especiales

- **Multilingüe**: Los modelos funcionan con múltiples idiomas (inglés, español, etc.)
- **Zero-shot**: No requiere entrenamiento previo para nuevas tareas de clasificación
- **Interactivo**: Interfaces web construidas con Gradio para fácil uso
- **Optimizado**: Uso de Faster-Whisper para transcripción eficiente

## 🔗 Enlaces

- [Notebook completo](../transcripcion_audio_whisper.ipynb)
- [Volver al índice de NLP](../README.md)

