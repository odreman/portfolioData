# Chatbot de Atención al Cliente con Gradio y OpenAI

## 📋 Descripción

Este proyecto implementa un chatbot de atención al cliente utilizando la biblioteca Gradio para la interfaz de usuario y la API de OpenAI para generar respuestas. El chatbot está configurado para una tienda de electrónica (TechWorld) y responde preguntas sobre productos específicos.

## 🎯 Objetivo

Implementar un chatbot completo que:
- Mantenga el historial de conversación para proporcionar respuestas coherentes
- Utilice la técnica de Chain of Thought (CoT) con mensajes de rol "system"
- Calcule y muestre el coste de cada consulta al API de OpenAI
- Proporcione respuestas restrictivas sobre productos específicos

## 📊 Configuración del Chatbot

El chatbot está configurado para responder solo sobre estos 5 productos específicos:
- Monitores
- Mouse
- Audífonos
- Web cam
- Micrófonos

Utiliza un mensaje de rol "system" altamente restrictivo que guía al asistente a seguir un proceso específico para cada consulta.

## 🛠️ Tecnologías Utilizadas

- **OpenAI API** - Modelos de lenguaje para generación de respuestas
- **Gradio** - Interfaz web interactiva
- **Python** - Lenguaje de programación

## 📖 Temas Cubiertos

- Chatbots con OpenAI API
- Gestión de historial de conversación
- Chain of Thought (CoT)
- Prompt engineering
- Cálculo de costes de API (tokens de entrada y salida)
- Interfaces web interactivas con Gradio
- Mensajes de rol "system" para controlar comportamiento del modelo

## 📁 Estructura del Proyecto

```
chatbot_atencion_cliente_openai/
├── README.md
└── chatbot_atencion_cliente_openai.ipynb
```

## 🚀 Ejecución

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install openai gradio
```

2. **Configuración de API Key**: Necesitas una clave API de OpenAI. Puedes:
   - Usar secretos de Google Colab: `userdata.get('OPENAI_API_KEY')`
   - O usar un archivo `.env` con `load_dotenv()` y `os.environ.get("OPENAI_API_KEY")`

3. Abre el notebook `chatbot_atencion_cliente_openai.ipynb` en Jupyter

4. Configura tu API key y ejecuta todas las celdas

## 📈 Resultados Clave

- Chatbot funcional con historial de conversación
- Respuestas coherentes y contextualizadas
- Control restrictivo sobre productos sobre los que puede responder
- Visualización del coste de cada consulta
- Interfaz web interactiva y fácil de usar

## 💡 Características Especiales

- **Chain of Thought**: El chatbot sigue un proceso estructurado para generar respuestas
- **Restrictivo**: Solo responde sobre productos específicos configurados
- **Transparente**: Muestra el coste de cada consulta para familiarizarse con el modelo de precios
- **Contextual**: Mantiene el historial de conversación para respuestas coherentes

## 🔗 Enlaces

- [Notebook completo](../chatbot_atencion_cliente_openai.ipynb)
- [Volver al índice de NLP](../README.md)

