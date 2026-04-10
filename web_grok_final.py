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

# --- ARQUITECTURA OVERLORD 2026 ---
# Configuración de página con el máximo ancho disponible
st.set_page_config(
    page_title="ANTHONY ULTRA-FLASH 2.0", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- IDENTIDAD DEL CREADOR (NO MODIFICAR) ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "v20.0 Quantum-Flash 2026"

# --- MÓDULOS DE INTELIGENCIA TÉCNICA (VERSION COMPLETA) ---

def super_rastreador_2026(query):
    """
    Escaneo satelital de noticias y mercados en tiempo real.
    Busca específicamente datos de 2026 en Ecuador.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        # Sincronización con la fecha actual del sistema: 10 de Abril 2026
        url = f"https://www.google.com/search?q={query}+Ecuador+hoy+10+abril+2026"
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        
        datos = []
        # Rastreo profundo de etiquetas de texto real
        for g in soup.find_all(['h3', 'div', 'span']):
            t = g.get_text().strip()
            if len(t) > 50:
                datos.append(f"📡 SEÑAL 2026: {t}")
        
        if not datos:
            return "El rastreador no encontró señales externas. Usando base de datos interna de Quinindé."
        return "\n".join(datos[:15])
    except Exception as e:
        return f"Error de enlace satelital: {str(e)}"

def interceptor_audiovisual(url):
    """
    Análisis profundo de videos de YouTube para extraer inteligencia.
    """
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            m = ydl.extract_info(url, download=False)
            resumen = f"""
            DETECCIÓN DE VIDEO:
            - Título: {m.get('title')}
            - Canal: {m.get('uploader')}
            - Fecha: {m.get('upload_date')}
            - Contenido Escaneado: {m.get('description')[:800]}...
            """
            return resumen
    except:
        return "⚠️ Alerta Overlord: Señal de video protegida o enlace inválido."

def generador_archivos_elite(texto_ia):
    """
    Generación masiva de documentos profesionales Word, Excel y PPT.
    Corregido para evitar errores de codificación.
    """
    f_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # 1. GENERACIÓN DE WORD (INFORME TITANIUM)
    doc = Document()
    doc.add_heading(f'REPORTE ESTRATÉGICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"OPERADOR CENTRAL: {CREADOR}")
    doc.add_paragraph(f"SEDE OPERATIVA: {SEDE}")
    doc.add_paragraph(f"FECHA DE EMISIÓN: {f_actual}")
    doc.add_heading('Análisis y Conclusiones:', level=1)
    doc.add_paragraph(texto_ia)
    
    bw = io.BytesIO()
    doc.save(bw)
    
    # 2. GENERACIÓN DE EXCEL (MATRIZ DE DATOS)
    df = pd.DataFrame({
        'ATRIBUTO': ['Operador', 'Sede', 'Motor de IA', 'Versión', 'Estado'],
        'VALOR': [CREADOR, SEDE, 'Gemini 2.0 Flash-Lite', VERSION, 'OPERATIVO']
    })
    be = io.BytesIO()
    with pd.ExcelWriter(be, engine='xlsxwriter') as wr:
        df.to_excel(wr, index=False, sheet_name='Reporte_Anthony')
    
    # 3. GENERACIÓN DE PPT (PRESENTACIÓN EJECUTIVA)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"ANÁLISIS 2026 - {CREADOR}"
    slide.placeholders[1].text = f"Resultados del Procesamiento Overlord:\n\n{texto_ia[:900]}..."
    
    bp = io.BytesIO()
    prs.save(bp)
    
    return bw.getvalue(), be.getvalue(), bp.getvalue()

# --- INTERFAZ SIDEBAR DE CONTROL ---
with st.sidebar:
    st.title("⚡ ULTRA-FLASH 2.0")
    st.markdown(f"**Nivel de Acceso:** Overlord")
    st.divider()
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 SEDE: {SEDE}")
    st.divider()
    
    # Botón de purga total
    if st.button("🚨 REINICIAR NÚCLEO CENTRAL"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.write(f"**Versión:** {VERSION}")

# --- MANEJO DE MEMORIA (CHAT HISTORY) ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Mostrar mensajes previos
for ch in st.session_state.chat_history:
    with st.chat_message(ch["role"]):
        st.markdown(ch["content"])

# --- PROCESAMIENTO DE COMANDOS CENTRAL ---
if prompt := st.chat_input("Inserta tus órdenes de nivel Overlord, Anthony..."):
    # Guardar en memoria
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Fase de preparación de datos
        with st.status("🚀 Procesando con Gemini 2.0 Flash-Lite...") as status:
            ctx_data = ""
            
            # Rastreo automático por palabras clave
            if any(k in prompt.lower() for k in ["noticia", "precio", "cacao", "hoy", "mercado", "dolar"]):
                st.write("🛰️ Escaneando satélites para datos de 2026...")
                ctx_data = super_rastreador_2026(prompt)
            
            # Interceptor de YouTube
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Interceptando señal de video...")
                ctx_data = interceptor_audiovisual(prompt)
                
            status.update(label="✅ Inteligencia lista. Generando respuesta técnica...", state="complete")

        try:
            # CONFIGURACIÓN DEL MOTOR 2.0 FLASH (ULTRA RÁPIDO)
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            model = genai.GenerativeModel('gemini-2.0-flash-lite-preview-02-05')
            
            instruccion_maestra = f"""
            Eres Anthony-Ultra Flash 2.0. Tu creador es {CREADOR}. 
            Tu sede operativa es {SEDE}. Hoy es Viernes 10 de Abril de 2026.
            
            DATA EN VIVO PARA ESTA RESPUESTA: {ctx_data}
            
            INSTRUCCIÓN: Responde de forma masiva, técnica, profesional y extremadamente actualizada. 
            No uses información vieja. Enfócate en la realidad del 2026.
            """
            
            # Llamada al núcleo
            respuesta = model.generate_content(f"{instruccion_maestra}\n\nORDEN DEL OPERADOR: {prompt}")
            texto_final = respuesta.text
            
            # Mostrar resultado
            st.markdown(texto_final)
            
            # --- FASE DE GENERACIÓN DE ENTREGABLES ---
            w, e, p = generador_archivos_elite(texto_final)
            
            st.divider()
            st.subheader("📦 PAQUETE TITANIUM GENERADO")
            col1, col2, col3 = st.columns(3)
            
            col1.download_button(
                label="📄 Informe Word Pro",
                data=w,
                file_name=f"Reporte_Elite_{CREADOR}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            col2.download_button(
                label="📈 Matriz de Datos Excel",
                data=e,
                file_name=f"Data_Titanium_{CREADOR}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            col3.download_button(
                label="📊 Presentación PPT",
                data=p,
                file_name=f"Analisis_Overlord_{CREADOR}.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
            
            # Guardar en memoria
            st.session_state.chat_history.append({"role": "assistant", "content": texto_final})

        except Exception as err:
            st.error(f"🚨 FALLA CRÍTICA EN EL NÚCLEO 2.0: {str(err)}")
            st.info("Anthony, revisa que tu llave de Google Gemini esté bien puesta en los Secrets.")
