import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io
import os
from datetime import datetime
import google.generativeai as genai

# --- ARQUITECTURA OVERLORD 2026 ---
st.set_page_config(
    page_title="ANTHONY TITÁN SUPREMO 2026", 
    page_icon="🔱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- IDENTIDAD Y CONFIGURACIÓN ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "v24.0 Force-Start 2026"
# LLAVE INTEGRADA PARA EVITAR ERRORES DE SECRETS
API_KEY_ANTHONY = "AIzaSyDsEVh_8vhE3_8qaO-kNctnsC8N8PVfVec"

# --- MÓDULOS DE INTELIGENCIA ---

def rastreador_2026(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.google.com/search?q={query}+Ecuador+2026"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        datos = [item.get_text() for item in soup.find_all(['h3', 'span']) if len(item.get_text()) > 50]
        return "\n".join(datos[:10])
    except:
        return "Sincronizando con memoria local..."

def constructor_archivos(texto):
    # Word
    doc = Document()
    doc.add_heading(f'REPORTE ANTHONY PRADO', 0)
    doc.add_paragraph(texto)
    bw = io.BytesIO(); doc.save(bw)
    # Excel
    df = pd.DataFrame({'SISTEMA': ['Anthony Titán'], 'ESTADO': ['ACTIVO']})
    be = io.BytesIO()
    with pd.ExcelWriter(be, engine='xlsxwriter') as wr: df.to_excel(wr, index=False)
    # PPT
    prs = Presentation(); slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "ANÁLISIS 2026"; slide.placeholders[1].text = texto[:500]
    bp = io.BytesIO(); prs.save(bp)
    return bw.getvalue(), be.getvalue(), bp.getvalue()

# --- INTERFAZ ---
with st.sidebar:
    st.title("🔱 TITÁN SUPREMO")
    st.success(f"OPERADOR: {CREADOR}")
    st.info(f"SEDE: {SEDE}")
    if st.button("🚨 REINICIAR"):
        st.session_state.chat_history = []
        st.rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

# --- LÓGICA DE DISPARO ---
# Si el botón no se presiona, es porque falta este bloque:
if prompt := st.chat_input("Escribe tus órdenes, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🚀 Procesando...", state="running"):
            ctx = rastreador_2026(prompt)
            try:
                genai.configure(api_key=API_KEY_ANTHONY)
                model = genai.GenerativeModel('gemini-1.5-flash') # Cambiado a Flash para asegurar velocidad
                res = model.generate_content(f"Eres Titán 2026 de Anthony Prado en Quinindé. Contexto: {ctx}. Orden: {prompt}")
                respuesta_texto = res.text
            except Exception as e:
                respuesta_texto = f"Error de conexión: {str(e)}"

        st.markdown(respuesta_texto)
        
        # Generar archivos
        w, e, p = constructor_archivos(respuesta_texto)
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.download_button("📄 Word", w, "Reporte.docx")
        c2.download_button("📈 Excel", e, "Datos.xlsx")
        c3.download_button("📊 PPT", p, "Presentacion.pptx")
        
        st.session_state.chat_history.append({"role": "assistant", "content": respuesta_texto})
