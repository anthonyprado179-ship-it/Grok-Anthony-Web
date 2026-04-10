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

# --- CONFIGURACIÓN DE PODER ABSOLUTO ---
st.set_page_config(page_title="GROK-ANTHONY ELITE 2026", page_icon="♾️", layout="wide")

# --- IDENTIDAD DEL CREADOR ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "v7.0 Titanium - 2026"

# --- FUNCIONES DE ALTO NIVEL (EL ARSENAL) ---

def super_buscador_google_2026(query):
    """Buscador profundo para capturar datos reales de 2026"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = f"https://www.google.com/search?q={query}+actualidad+2026+ecuador"
        r = requests.get(url, headers=headers, timeout=12)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        fragmentos = []
        for g in soup.find_all(['h3', 'div'], class_=['BNeawe', 'vv4Sgc', 'tF2Cxc']):
            txt = g.get_text().strip()
            if len(txt) > 35:
                fragmentos.append(f"• {txt}")
        
        return "\n".join(fragmentos[:12]) if fragmentos else "No se detectaron cambios externos. Operando con proyecciones internas 2026."
    except Exception as e:
        return f"Error en rastreo satelital: {str(e)}"

def interceptor_youtube_2026(url):
    """Escaneo y resumen de videos de alta definición"""
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            return f"""
            DATOS DEL VIDEO INTERCEPTADO:
            - Título: {meta.get('title')}
            - Autor: {meta.get('uploader')}
            - Vistas: {meta.get('view_count')}
            - Resumen Técnico: {meta.get('description')[:900]}...
            """
    except:
        return "⚠️ Error: El video está protegido o la señal es inestable."

def generar_paquete_oficina_2026(texto_ia):
    """Generación masiva de documentos Word, Excel y Powerpoint con un solo clic"""
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # --- WORD PROFESIONAL ---
    doc = Document()
    doc.add_heading(f'INFORME ESTRATÉGICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"FECHA: {fecha_hoy} | SEDE: {SEDE}")
    doc.add_heading('Análisis de Inteligencia Artificial:', level=1)
    doc.add_paragraph(texto_ia)
    buf_word = io.BytesIO()
    doc.save(buf_word)
    
    # --- EXCEL ANALÍTICO ---
    df_data = pd.DataFrame({
        'PARÁMETRO': ['Operador Central', 'Ubicación Geográfica', 'Estado del Sistema', 'Versión de Núcleo', 'Timestamp'],
        'VALOR': [CREADOR, SEDE, 'OPERATIVO', VERSION, fecha_hoy]
    })
    buf_excel = io.BytesIO()
    with pd.ExcelWriter(buf_excel, engine='xlsxwriter') as writer:
        df_data.to_excel(writer, index=False, sheet_name='Reporte_Anthony_2026')
    
    # --- POWERPOINT DE PRESENTACIÓN ---
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"REPORTE 2026: {CREADOR}"
    slide.placeholders[1].text = f"Resultados del procesamiento:\n\n{texto_ia[:850]}..."
    buf_ppt = io.BytesIO()
    prs.save(buf_ppt)
    
    return buf_word.getvalue(), buf_excel.getvalue(), buf_ppt.getvalue()

# --- INTERFAZ DE CONTROL (SIDEBAR) ---
with st.sidebar:
    st.markdown(f"### ♾️ {VERSION}")
    st.divider()
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 UBICACIÓN: {SEDE}")
    st.divider()
    
    st.header("📂 INYECTOR DE ARCHIVOS")
    archivo_subido = st.file_uploader("Subir PDF, CSV o TXT para análisis", type=["csv", "txt", "pdf"])
    if archivo_subido:
        st.warning("Datos inyectados en la memoria volátil.")
        
    st.divider()
    if st.button("🚨 PURGAR MEMORIA CENTRAL"):
        st.session_state.chat_history = []
        st.rerun()

# --- HISTORIAL DE COMANDOS ---
if "chat_history" not in st.session_state:
    st.session_state.history_raw = []
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- PROCESAMIENTO DE ÓRDENES ---
if prompt := st.chat_input("Escribe tus órdenes, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Activando protocolos Overlord 2026...") as status:
            contexto_en_vivo = ""
            
            # Rastreo automático
            if any(k in prompt.lower() for k in ["noticia", "precio", "hoy", "mercado", "cacao", "dolar", "clima"]):
                st.write("🛰️ Escaneando satélites de Google 2026...")
                contexto_en_vivo = super_buscador_google_2026(prompt)
            
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Interceptando señal de video...")
                contexto_en_vivo = interceptor_youtube_2026(prompt)
                
            status.update(label="✅ Datos listos. Ejecutando Grok...", state="complete")

        try:
            # CONEXIÓN CON LA API (CON CORRECCIÓN DE MODELO)
            headers = {
                "Authorization": f"Bearer {st.secrets['XAI_API_KEY']}",
                "Content-Type": "application/json"
            }
            
            # Cambiamos a 'grok-beta' que es el que acepta todas las llaves nuevas
            payload = {
                "model": "grok-beta", 
                "messages": [
                    {
                        "role": "system", 
                        "content": f"""Eres Grok-Anthony Overlord. Fecha Actual: Abril 2026. 
                        Creador: {CREADOR}. Sede: {SEDE}. 
                        ESTILO: Técnico, agresivo, ultra-actualizado. 
                        DATA EN VIVO: {contexto_en_vivo}."""
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.4
            }

            r = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
            
            # --- BLINDAJE ANTI-ERRORES 'STR' ---
            try:
                data_json = r.json()
            except:
                data_json = {"error": {"message": f"Fallo de servidor: {r.text}"}}

            if 'choices' in data_json:
                final_res = data_json['choices'][0]['message']['content']
                st.markdown(final_res)
                
                # Generación masiva de archivos
                w, e, p = generar_paquete_oficina_2026(final_res)
                
                st.divider()
                st.subheader("📦 PAQUETE DE ENTREGABLES GENERADO")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Word Profesional", w, f"Reporte_{CREADOR}.docx")
                c2.download_button("📈 Análisis Excel", e, f"Data_{CREADOR}.xlsx")
                c3.download_button("📊 Presentación PPT", p, f"Resumen_{CREADOR}.pptx")
                
                st.session_state.chat_history.append({"role": "assistant", "content": final_res})
            else:
                # Captura de error de modelo o llave
                err_data = data_json.get('error', {})
                msg = err_data.get('message', 'Error desconocido') if isinstance(err_data, dict) else str(err_data)
                st.error(f"⚠️ SISTEMA BLOQUEADO: {msg}")
                st.info("Sugerencia: Revisa si tu llave tiene créditos en console.x.ai")

        except Exception as e:
            st.error(f"🚨 FALLA CRÍTICA EN EL NÚCLEO: {str(e)}")
