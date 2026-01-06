# client.py
import requests
import streamlit as st
from typing import Dict, Any
import json

# Configuración de la página
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🤖 AI Content Generator")
st.markdown("*Genera texto, audio e imágenes con inteligencia artificial*")

# Configuración de la API
API_BASE_URL = "http://localhost:8000"

# Sidebar para configuraciones
with st.sidebar:
    st.header("⚙️ Configuraciones")
    
    # Selección de modo
    mode = st.selectbox(
        "Modo de generación",
        ["🧠 Inteligente (Auto-detecta)", "📝 Solo Texto", "🎵 Solo Audio", "🎨 Solo Imagen"],
        index=0
    )
    
    # Configuraciones específicas
    if mode in ["🧠 Inteligente (Auto-detecta)", "📝 Solo Texto"]:
        temperature = st.slider("Temperatura (creatividad)", 0.1, 1.0, 0.7, 0.1)
    
    if mode in ["🧠 Inteligente (Auto-detecta)", "🎵 Solo Audio"]:
        voice_preset = st.selectbox(
            "Voz para audio",
            ["v2/en_speaker_1", "v2/en_speaker_2", "v2/en_speaker_3", 
             "v2/en_speaker_4", "v2/en_speaker_5", "v2/en_speaker_6",
             "v2/en_speaker_7", "v2/en_speaker_8", "v2/en_speaker_9"],
            index=0
        )
    
    st.markdown("---")
    st.markdown("### 💡 Consejos de uso:")
    st.markdown("""
    **Para texto:** Haz preguntas o pide explicaciones
    
    **Para audio:** Usa palabras como "di", "habla", "pronuncia"
    
    **Para imágenes:** Usa palabras como "imagen", "foto", "dibujo"
    """)

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        elif message["type"] == "image":
            st.image(message["content"])
        elif message["type"] == "audio":
            st.audio(message["content"])
        elif message["type"] == "mixed":
            # Para respuestas mixtas del modo inteligente
            if "text" in message["content"]:
                st.markdown(message["content"]["text"])
            if "image" in message["content"]:
                st.image(message["content"]["image"])
            if "audio" in message["content"]:
                st.audio(message["content"]["audio"])

# Input del usuario
if prompt := st.chat_input("Escribe tu prompt aquí..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt, 
        "type": "text"
    })
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Procesar según el modo seleccionado
    with st.chat_message("assistant"):
        with st.spinner("Generando contenido..."):
            try:
                if mode == "📝 Solo Texto":
                    # Generar solo texto
                    response = requests.get(
                        f"{API_BASE_URL}/generate/text",
                        params={"prompt": prompt, "temperature": temperature}
                    )
                    response.raise_for_status()
                    
                    text_content = response.text.strip('"')
                    st.markdown(text_content)
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": text_content,
                        "type": "text"
                    })
                
                elif mode == "🎵 Solo Audio":
                    # Generar solo audio
                    response = requests.get(
                        f"{API_BASE_URL}/generate/audio",
                        params={"prompt": prompt, "preset": voice_preset}
                    )
                    response.raise_for_status()
                    
                    st.success("Audio generado exitosamente!")
                    st.audio(response.content, format="audio/wav")
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response.content,
                        "type": "audio"
                    })
                
                elif mode == "🎨 Solo Imagen":
                    # Generar solo imagen
                    response = requests.get(
                        f"{API_BASE_URL}/generate/image",
                        params={"prompt": prompt}
                    )
                    response.raise_for_status()
                    
                    st.success("Imagen generada exitosamente!")
                    st.image(response.content)
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response.content,
                        "type": "image"
                    })
                
                elif mode == "🧠 Inteligente (Auto-detecta)":
                    # Usar el endpoint inteligente
                    response = requests.get(
                        f"{API_BASE_URL}/generate/smart",
                        params={
                            "prompt": prompt, 
                            "voice_preset": voice_preset,
                            "temperature": temperature
                        }
                    )
                    response.raise_for_status()
                    
                    data = response.json()
                    
                    # Mostrar respuesta de texto
                    st.markdown("**Respuesta:**")
                    st.markdown(data["text_response"])
                    
                    # Mostrar tipo detectado
                    st.info(f"Tipo detectado: {data['detected_type']}")
                    
                    # Contenido adicional según el tipo
                    mixed_content = {"text": data["text_response"]}
                    
                    if data["detected_type"] == "image":
                        st.markdown("**Imagen generada:**")
                        try:
                            img_response = requests.get(
                                f"{API_BASE_URL}/generate/image",
                                params={"prompt": data.get("image_prompt", prompt)}
                            )
                            img_response.raise_for_status()
                            st.image(img_response.content)
                            mixed_content["image"] = img_response.content
                        except Exception as e:
                            st.error(f"Error generando imagen: {str(e)}")
                    
                    elif data["detected_type"] == "audio":
                        st.markdown("**Audio generado:**")
                        try:
                            audio_response = requests.get(
                                f"{API_BASE_URL}/generate/audio",
                                params={
                                    "prompt": data.get("audio_prompt", prompt),
                                    "preset": voice_preset
                                }
                            )
                            audio_response.raise_for_status()
                            st.audio(audio_response.content, format="audio/wav")
                            mixed_content["audio"] = audio_response.content
                        except Exception as e:
                            st.error(f"Error generando audio: {str(e)}")
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": mixed_content,
                        "type": "mixed"
                    })
                
            except requests.exceptions.RequestException as e:
                st.error(f"Error de conexión: {str(e)}")
                st.info("Asegúrate de que la API esté ejecutándose en http://localhost:8000")
            except Exception as e:
                st.error(f"Error inesperado: {str(e)}")

# Botón para limpiar historial
if st.sidebar.button("🗑️ Limpiar Historial"):
    st.session_state.messages = []
    st.rerun()

# Información adicional en el sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🔧 Estado de la API")
    
    # Verificar estado de la API
    try:
        health_response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if health_response.status_code == 200:
            st.success("✅ API Conectada")
        else:
            st.error("❌ API con problemas")
    except:
        st.error("❌ API Desconectada")
    
    st.markdown("---")
    st.markdown("### 📊 Estadísticas")
    st.metric("Mensajes en historial", len(st.session_state.messages))
    
    # Contar tipos de contenido
    text_count = sum(1 for msg in st.session_state.messages if msg.get("type") == "text")
    audio_count = sum(1 for msg in st.session_state.messages if msg.get("type") == "audio")
    image_count = sum(1 for msg in st.session_state.messages if msg.get("type") == "image")
    mixed_count = sum(1 for msg in st.session_state.messages if msg.get("type") == "mixed")
    
    if text_count > 0:
        st.metric("Respuestas de texto", text_count)
    if audio_count > 0:
        st.metric("Audios generados", audio_count)
    if image_count > 0:
        st.metric("Imágenes generadas", image_count)
    if mixed_count > 0:
        st.metric("Respuestas mixtas", mixed_count)