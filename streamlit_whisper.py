import streamlit as st
import whisper

# Título de la aplicación
st.title("Whisper App")

# Subir archivo de audio con Streamlit
audio_file = st.file_uploader("Subir Audio", type=["wav", "mp3", "m4a"])

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Verificar si se cargó el modelo correctamente
st.text("Modelo de Whisper Cargado")

# Botón para transcribir el audio
if st.sidebar.button("Transcribir Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribiendo Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcripción Completa")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Por favor, carga un archivo de audio")

# Reproducir el archivo de audio original
st.sidebar.header("Reproducir Archivo de Audio Original")
st.sidebar.audio(audio_file)

