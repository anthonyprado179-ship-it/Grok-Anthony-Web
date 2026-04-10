import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io
import time
from datetime import datetime

# --- ARQUITECTURA DE PODER TOTAL 2026 ---
st.set_page_config(page_title="ANTHONY MULTI-ENGINE 2026", page_icon="🔱", layout="wide")

# --- IDENTIDAD DEL SISTEMA ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
FECHA_SISTEMA = "10 de Abril, 2026"
VERSION = "v11.0 Gold Edition"

# --- MÓDULOS DE INTELIGENCIA DE CAMPO (NO SE QUITA NADA) ---

def buscador_profundo_google_2026(query):
    """Rastreo satelital de noticias y precios en tiempo real"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = f"https://www.google.com/search?q={query}+actualidad+2026+ecuador"
        r = requests.get(url, headers=headers, timeout=12)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        fragmentos = []
        # Capturamos títulos y párrafos descriptivos
        for g in soup.find_all(['h3', 'div', 'span']):
            txt = g.get_text().strip()
            if len(txt) > 40:
                fragmentos.append(f"• {txt}")
        
        return "\n".join(fragmentos[:12]) if fragmentos else "Usando proyecciones de base de datos Anthony-OS 2026."
    except Exception as e:
        return f"Error en enlace de datos: {str(e)}"

def interceptor_youtube_2026(url):
    """Escaneo y extracción de metadatos de video"""
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            return f"""
            ANÁLISIS TÉCNICO DE VIDEO:
            - Título: {meta.get('title')}
            - Creador: {meta.get('uploader')}
            - Fecha: {meta.get('upload_date')}
            - Resumen: {meta.get('description')[:800]}...
            """
    except:
        return "⚠️ Señal de video encriptada o fuera de alcance."

def generar_suite_corporativa_2026(texto_ia):
    """Generación masiva de documentos Word, Excel y Powerpoint"""
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # 1. GENERACIÓN WORD PROFESIONAL
    doc = Document()
    doc.add_heading(f'INFORME TÉCNICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"FECHA: {fecha_hoy} | UBICACIÓN: {SEDE}")
    doc.add_heading('Conclusiones del Sistema:', level=1)
    doc.add_paragraph(texto_ia)
    buf_word = io.BytesIO()
    doc.save(buf_word)
    
    # 2. GENERACIÓN EXCEL DE DATOS
    df_data = pd.DataFrame({
        'PARÁMETRO': ['Operador Central', 'Estado', 'Versión', 'Ubicación'],
        'VALOR': [CREADOR, 'OPERATIVO', VERSION, SEDE]
    })
    buf_excel = io.BytesIO()
    with pd.ExcelWriter(buf_excel, engine='xlsxwriter') as writer:
        df_data.to_excel(writer, index=False, sheet_name='Reporte_Anthony_2026')
    
    # 3. GENERACIÓN POWERPOINT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"REPORTE 2026: {CREADOR}"
    slide.placeholders[1].text = f"Resultados del Análisis:\n\n{texto_ia[:850]}..."
    buf_ppt = io.BytesIO()
    prs.save(buf_ppt)
    
    return buf_word.getvalue(), buf_excel.getvalue(), buf_ppt.getvalue()

# --- INTERFAZ LATERAL (CONTROL DE MANDO) ---
with st.sidebar:
    st.markdown(f"### 🔱 {VERSION}")
    st.divider()
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 SEDE: {SEDE}")
    
    st.divider()
    st.header("⚙️ CONFIGURACIÓN")
    # Este motor permite usar IA GRATIS
    motor_ia = st.selectbox("Motor de Inteligencia:", ["Google Gemini (Gratis)", "Llama 3 (Gratis)"])
    
    st.divider()
    if st.button("🚨 PURGAR MEMORIA CENTRAL"):
        st.session_state.chat_history = []
        st.rerun()

# --- HISTORIAL DE CONVERSACIÓN ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- NÚCLEO DE PROCESAMIENTO ---
if prompt := st.chat_input("Escribe tus órdenes, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Activando protocolos 2026...") as status:
            contexto_en_vivo = ""
            
            # Rastreo automático por palabras clave
            if any(k in prompt.lower() for k in ["noticia", "precio", "hoy", "cacao", "dolar", "mercado"]):
                st.write("🛰️ Escaneando satélites de búsqueda...")
                contexto_en_vivo = buscador_profundo_google_2026(prompt)
            
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Interceptando señal de video...")
                contexto_en_vivo = interceptor_youtube_2026(prompt)
                
            status.update(label="✅ Inteligencia recolectada. Procesando...", state="complete")

        try:
            # --- CONEXIÓN A OPENROUTER (LA LLAVE PARA USAR IA GRATIS) ---
            api_key = st.secrets["OPENROUTER_API_KEY"]
            url_openrouter = "https://openrouter.ai/api/v1/chat/completions"
            
            # Mapeo de modelos gratis
            modelo_seleccionado = "google/gemini-2.0-flash-exp:free"
            if "Llama" in motor_ia:
                modelo_seleccionado = "meta-llama/llama-3.3-70b-instruct:free"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8501", # Obligatorio para OpenRouter
                "X-Title": "Anthony Overlord 2026"
            }
            
            payload = {
                "model": modelo_seleccionado,
                "messages": [
                    {
                        "role": "system", 
                        "content": f"Eres Anthony Overlord. Fecha Actual: Abril 2026. Creador: {CREADOR}. Sede: {SEDE}. DATA EN VIVO: {contexto_en_vivo}. Responde de forma masiva y técnica."
                    },
                    {"role": "user", "content": prompt}
                ]
            }

            r = requests.post(url_openrouter, headers=headers, json=payload)
            data_json = r.json()

            if 'choices' in data_json:
                res_final = data_json['choices'][0]['message']['content']
                st.markdown(res_final)
                
                # GENERACIÓN DE ENTREGABLES
                w, e, p = generar_suite_corporativa_2026(res_final)
                
                st.divider()
                st.subheader("📦 PAQUETE DE ENTREGABLES GENERADO")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Informe Word", w, f"Reporte_{CREADOR}.docx")
                c2.download_button("📈 Análisis Excel", e, f"Data_{CREADOR}.xlsx")
                c3.download_button("📊 Diapositivas PPT", p, f"Resumen_{CREADOR}.pptx")
                
                st.session_state.chat_history.append({"role": "assistant", "content": res_final})
            else:
                error_info = data_json.get('error', {})
                st.error(f"⚠️ Error de Motor: {error_info.get('message', 'Falla de conexión')}")

        except Exception as e:
            st.error(f"🚨 Falla Crítica en el Núcleo: {str(e)}")
