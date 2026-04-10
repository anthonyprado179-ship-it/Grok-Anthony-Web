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

# --- 1. ARQUITECTURA OVERLORD 2026 ---
st.set_page_config(
    page_title="ANTHONY TITÁN SUPREMO 2026", 
    page_icon="🔱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. IDENTIDAD Y NÚCLEO DE PODER ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "v25.0 Hyper-Titanium"
# INYECCIÓN DIRECTA DE LA NUEVA API KEY
API_KEY_ANTHONY = "AIzaSyA9Y05FosTiw4DTksSeDZGtdMF8s9Z_RH0"

# --- 3. MÓDULOS TÉCNICOS DE ALTO NIVEL ---

def rastreador_satelital_2026(query):
    """Escaneo de noticias y precios de cacao en tiempo real"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = f"https://www.google.com/search?q={query}+Ecuador+abril+2026"
        r = requests.get(url, headers=headers, timeout=12)
        soup = BeautifulSoup(r.text, 'html.parser')
        datos = [t.get_text().strip() for t in soup.find_all(['h3', 'div', 'span']) if len(t.get_text()) > 60]
        return "\n".join(datos[:12]) if datos else "Usando base de datos local de Quinindé."
    except Exception as e:
        return f"Sincronización limitada: {str(e)}"

def constructor_suite_documental(texto_ia):
    """Generador masivo de Word, Excel y PowerPoint"""
    # WORD
    doc = Document()
    doc.add_heading(f'REPORTE ESTRATÉGICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"OPERADOR: {CREADOR} | SEDE: {SEDE} | 2026")
    doc.add_paragraph(texto_ia)
    bw = io.BytesIO(); doc.save(bw)
    
    # EXCEL
    df = pd.DataFrame({
        'ATRIBUTO': ['Operador', 'Sede', 'Estado', 'Motor'], 
        'VALOR': [CREADOR, SEDE, 'ACTIVO', 'Gemini 1.5 Flash']
    })
    be = io.BytesIO()
    with pd.ExcelWriter(be, engine='xlsxwriter') as wr: df.to_excel(wr, index=False)
    
    # PPT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"ANALISIS 2026 - {CREADOR}"
    slide.placeholders[1].text = f"Resultados:\n\n{texto_ia[:900]}"
    bp = io.BytesIO(); prs.save(bp)
    
    return bw.getvalue(), be.getvalue(), bp.getvalue()

# --- 4. INTERFAZ Y SIDEBAR ---
with st.sidebar:
    st.title("🔱 TITÁN SUPREMO")
    st.divider()
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 SEDE: {SEDE}")
    st.write(f"**Versión:** {VERSION}")
    st.divider()
    if st.button("🚨 REINICIAR SISTEMA"):
        st.session_state.chat_history = []
        st.rerun()

# --- 5. LÓGICA DE MEMORIA Y CHAT ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

# --- 6. PROCESAMIENTO CENTRAL (EL BOTÓN) ---
if prompt := st.chat_input("Inserta tus comandos, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Procesando con Inteligencia 2026...", state="running") as status:
            # Rastreo de datos
            ctx = ""
            if any(k in prompt.lower() for k in ["noticia", "precio", "cacao", "hoy", "mercado"]):
                ctx = rastreador_satelital_2026(prompt)
            
            # Llamada al Motor Gemini
            try:
                genai.configure(api_key=API_KEY_ANTHONY)
                model = genai.GenerativeModel('gemini-1.5-flash')
                respuesta = model.generate_content(f"Eres Titán 2026, la IA de Anthony Prado. Contexto: {ctx}. Orden: {prompt}")
                txt_final = respuesta.text
            except Exception as e:
                txt_final = f"🚨 ERROR DE LLAVE: {str(e)}. Anthony, verifica si esta llave está habilitada en Google AI Studio."
            
            status.update(label="✅ Procesamiento completo", state="complete")

        st.markdown(txt_final)
        
        # Generación de archivos descargables
        if "ERROR" not in txt_final:
            w, e, p = constructor_suite_documental(txt_final)
            st.divider()
            st.subheader("📦 PAQUETE TITANIUM")
            c1, c2, c3 = st.columns(3)
            c1.download_button("📄 Word Pro", w, f"Reporte_{CREADOR}.docx")
            c2.download_button("📈 Excel Data", e, f"Matriz_{CREADOR}.xlsx")
            c3.download_button("📊 PPT Resumen", p, f"Presentacion_{CREADOR}.pptx")
            
            st.session_state.chat_history.append({"role": "assistant", "content": txt_final})
