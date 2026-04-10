import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io
import os
import time
from datetime import datetime
import google.generativeai as genai

# --- ARQUITECTURA OVERLORD 2026: CONFIGURACIÓN SUPREMA ---
st.set_page_config(
    page_title="ANTHONY TITÁN SUPREMO 2026", 
    page_icon="🔱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- IDENTIDAD DEL SISTEMA ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "v23.0 Final-Titanium 2026"
FECHA_SISTEMA = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# --- MÓDULOS DE INTELIGENCIA DE ALTO NIVEL ---

def rastreador_satelital_2026(query):
    """
    Rastreo profundo de datos: Captura precios de cacao, noticias de Esmeraldas
    y tendencias de Ecuador en tiempo real (Abril 2026).
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
        # Búsqueda forzada a la actualidad de 2026
        url = f"https://www.google.com/search?q={query}+Ecuador+abril+2026+actualidad+precios"
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        
        hallazgos = []
        # Extracción técnica de fragmentos informativos
        for item in soup.find_all(['h3', 'div', 'span']):
            texto = item.get_text().strip()
            if len(texto) > 65:
                hallazgos.append(f"📡 SEÑAL 2026: {texto}")
        
        return "\n".join(hallazgos[:15]) if hallazgos else "Utilizando base de datos interna optimizada de Anthony-OS."
    except Exception as e:
        return f"Aviso: Sincronización externa limitada ({str(e)})"

def interceptor_youtube_titan(url):
    """
    Interceptor de YouTube: Escanea y resume videos extrayendo inteligencia estratégica.
    """
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            resumen = f"""
            DETECCIÓN MULTIMEDIA:
            - Título del Video: {info.get('title')}
            - Canal Emisor: {info.get('uploader')}
            - Resumen de Datos: {info.get('description')[:900]}...
            """
            return resumen
    except:
        return "⚠️ Alerta: Señal de video protegida o enlace no válido."

def generador_suite_oficina_2026(texto_ia):
    """
    Constructor de archivos corporativos: Genera Word, Excel y PowerPoint
    con formato profesional para Anthony Prado.
    """
    # 1. GENERACIÓN DE WORD (INFORME TÉCNICO)
    doc = Document()
    doc.add_heading(f'INFORME ESTRATÉGICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"OPERADOR CENTRAL: {CREADOR}")
    doc.add_paragraph(f"SEDE OPERATIVA: {SEDE}")
    doc.add_paragraph(f"FECHA DE GENERACIÓN: {FECHA_SISTEMA}")
    doc.add_heading('Análisis y Conclusiones de Inteligencia:', level=1)
    doc.add_paragraph(texto_ia)
    
    b_word = io.BytesIO()
    doc.save(b_word)
    
    # 2. GENERACIÓN DE EXCEL (MATRIZ DE DATOS)
    df = pd.DataFrame({
        'PARÁMETRO': ['Creador', 'Ubicación', 'Motor IA', 'Estado', 'Versión'],
        'VALOR': [CREADOR, SEDE, 'Gemini 2.0 Flash', 'ESTABLE', VERSION]
    })
    b_excel = io.BytesIO()
    with pd.ExcelWriter(b_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Reporte_2026')
    
    # 3. GENERACIÓN DE PPT (DIAPOSITIVAS)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"ANALISIS OVERLORD 2026 - {CREADOR}"
    slide.placeholders[1].text = f"Resultados Finales del Procesamiento:\n\n{texto_ia[:950]}..."
    
    b_ppt = io.BytesIO()
    prs.save(b_ppt)
    
    return b_word.getvalue(), b_excel.getvalue(), b_ppt.getvalue()

# --- INTERFAZ SIDEBAR DE CONTROL ---
with st.sidebar:
    st.title("🔱 TITÁN SUPREMO")
    st.markdown(f"**Nivel de Acceso:** Overlord")
    st.divider()
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 SEDE: {SEDE}")
    st.divider()
    
    if st.button("🚨 REINICIAR NÚCLEO CENTRAL"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.write(f"**Status:** Motor 2.0 Conectado")

# --- MANEJO DE MEMORIA (CHAT) ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- PROCESAMIENTO DE COMANDOS CENTRAL ---
if prompt := st.chat_input("Inserta tus órdenes, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🚀 Sincronizando con Google Gemini 2.0...") as status:
            contexto_ia = ""
            
            # Rastreador de mercado y noticias
            if any(k in prompt.lower() for k in ["noticia", "precio", "cacao", "hoy", "mercado", "dolar", "clima"]):
                st.write("🛰️ Escaneando satélites informativos...")
                contexto_ia = rastreador_satelital_2026(prompt)
            
            # Interceptor de YouTube
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Analizando flujo de video...")
                contexto_ia = interceptor_youtube_titan(prompt)
                
            status.update(label="✅ Inteligencia lista. Generando respuesta...", state="complete")

        try:
            # CONFIGURACIÓN DEL MOTOR GEMINI 2.0 FLASH (ULTRA-RÁPIDO)
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            instruccion_maestra = f"""
            Eres Anthony-Titán Supremo 2026. Tu creador es {CREADOR}. 
            Tu sede operativa es {SEDE}. Hoy es {FECHA_SISTEMA}.
            DATA EN VIVO: {contexto_ia}.
            Responde de forma masiva, técnica, profesional y extremadamente detallada. 
            Prioriza siempre la realidad del año 2026 en Ecuador.
            """
            
            # Generación de la respuesta final
            response = model.generate_content(f"{instruccion_maestra}\n\nORDEN: {prompt}")
            res_texto = response.text
            
            st.markdown(res_texto)
            
            # GENERACIÓN DE ENTREGABLES CORPORATIVOS
            w, e, p = generador_suite_oficina_2026(res_texto)
            
            st.divider()
            st.subheader("📦 PAQUETE CORPORATIVO GENERADO")
            c1, c2, c3 = st.columns(3)
            
            c1.download_button("📄 Informe Word Pro", w, f"Reporte_{CREADOR}.docx")
            c2.download_button("📈 Matriz Excel", e, f"Data_{CREADOR}.xlsx")
            c3.download_button("📊 PPT Resumen", p, f"Analisis_{CREADOR}.pptx")
            
            st.session_state.chat_history.append({"role": "assistant", "content": res_texto})

        except Exception as err:
            st.error(f"🚨 FALLA CRÍTICA EN EL NÚCLEO: {str(err)}")
            st.info("Revisa que tu API KEY esté bien pegada en los Secrets de Streamlit.")
