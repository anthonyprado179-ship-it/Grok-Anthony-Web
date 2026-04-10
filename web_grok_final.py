import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
import requests
from bs4 import BeautifulSoup
import io
import os
from datetime import datetime
# CAMBIO TÉCNICO: Usamos el nuevo motor de Google
import google.generativeai as genai

# CONFIGURACIÓN
st.set_page_config(page_title="ANTHONY TITÁN 2026", page_icon="🔱", layout="wide")

# --- IDENTIDAD Y PODER ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
# TU NUEVA KEY AQUÍ
API_KEY_ANTHONY = "AIzaSyA9Y05FosTiw4DTksSeDZGtdMF8s9Z_RH0"

# CONFIGURAR EL MOTOR UNA SOLA VEZ AL PRINCIPIO
genai.configure(api_key=API_KEY_ANTHONY)

# --- INTERFAZ ---
with st.sidebar:
    st.title("🔱 TITÁN SUPREMO")
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 {SEDE}")
    if st.button("🚨 REINICIAR SISTEMA"):
        st.session_state.chat_history = []; st.rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# MOSTRAR CHAT
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

# --- PROCESAMIENTO CENTRAL ---
if prompt := st.chat_input("Escribe tus órdenes, Anthony..."):
    # Guardar y mostrar lo que escribe Anthony
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Usamos el modelo estable para evitar el aviso de error
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Generar respuesta
            response = model.generate_content(f"Eres la IA de Anthony Prado. Hoy es 10 de abril de 2026. Ubicación: Quinindé. Orden: {prompt}")
            texto_final = response.text
            
            st.markdown(texto_final)
            st.session_state.chat_history.append({"role": "assistant", "content": texto_final})
            
        except Exception as e:
            st.error(f"Falla en el núcleo: {str(e)}")
            st.info("Anthony, si dice 'API_KEY_INVALID', revisa que la Key no tenga espacios extra.")
