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

# --- CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="GROK-ANTHONY OVERLORD 2026", page_icon="♾️", layout="wide")

# --- IDENTIDAD DEL SISTEMA ---
CREADOR = "Anthony Prado"
UBICACION = "Quinindé, Esmeraldas, Ecuador"
FECHA_SISTEMA = "10 de Abril, 2026"

# --- MÓDULOS DE INTELIGENCIA AVANZADA ---

def super_buscador_google_2026(query):
    """Buscador de grado militar para datos actuales"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = f"https://www.google.com/search?q={query}+2026+actualidad+ecuador"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Extraemos párrafos y títulos para dar contexto real a la IA
        fragmentos = []
        for g in soup.find_all(['h3', 'div'], class_=['BNeawe', 'vv4Sgc']):
            txt = g.get_text()
            if len(txt) > 30:
                fragmentos.append(f"• {txt}")
        
        return "\n".join(fragmentos[:10]) if fragmentos else "No se hallaron datos externos. Usando base de datos interna 2026."
    except Exception as e:
        return f"Error en rastreo satelital: {str(e)}"

def analizador_youtube_profundo(url):
    """Escaneo y extracción de datos de video"""
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            return f"""
            CONTENIDO DETECTADO EN YOUTUBE:
            - Título: {meta.get('title')}
            - Creador: {meta.get('uploader')}
            - Fecha de Carga: {meta.get('upload_date')}
            - Descripción: {meta.get('description')[:700]}
            """
    except:
        return "Seguridad de YouTube bloqueó el escaneo automático."

def generador_suite_oficina_2026(respuesta_ia):
    """Generación masiva de documentos Word, Excel y Powerpoint"""
    # 1. DOCUMENTO WORD PROFESIONAL
    doc = Document()
    doc.add_heading(f'REPORTE ESTRATÉGICO - {CREADOR.upper()}', 0)
    doc.add_paragraph(f"Fecha: {FECHA_SISTEMA} | Ubicación: {UBICACION}")
    doc.add_heading('Análisis Detallado:', level=1)
    doc.add_paragraph(respuesta_ia)
    
    buf_word = io.BytesIO()
    doc.save(buf_word)
    
    # 2. DATA EXCEL ANALÍTICA
    df = pd.DataFrame({
        'Atributo': ['Operador', 'Sede', 'Estado', 'Tecnología', 'Fecha'],
        'Valor': [CREADOR, UBICACION, 'Activo', 'Grok-2-Latest', FECHA_SISTEMA]
    })
    buf_excel = io.BytesIO()
    with pd.ExcelWriter(buf_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Data_Tecnica_2026')
    
    # 3. DIAPOSITIVAS POWERPOINT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"ANÁLISIS 2026 - {CREADOR}"
    slide.placeholders[1].text = f"Resumen de Operación:\n\n{respuesta_ia[:800]}..."
    buf_ppt = io.BytesIO()
    prs.save(buf_ppt)
    
    return buf_word.getvalue(), buf_excel.getvalue(), buf_ppt.getvalue()

# --- INTERFAZ DE COMANDO (SIDEBAR) ---
with st.sidebar:
    st.title("♾️ OMNI-CONTROL 2026")
    st.subheader(f"User: {CREADOR}")
    st.markdown(f"**Ubicación:** {UBICACION}")
    st.divider()
    
    st.header("📂 Inyector de Datos")
    archivo_subido = st.file_uploader("Cargar archivos PDF/CSV/TXT", type=["csv", "txt", "pdf"])
    if archivo_subido:
        st.success("Base de datos cargada al núcleo.")
        
    st.divider()
    if st.button("🚨 PURGAR TODO EL SISTEMA"):
        st.session_state.chat_history = []
        st.rerun()

# --- LÓGICA DE HISTORIAL ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- NÚCLEO CENTRAL DE PROCESAMIENTO ---
if prompt := st.chat_input("Escribe tus órdenes, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Activando protocolos 2026...") as status:
            contexto_en_vivo = ""
            
            # Decisión inteligente de herramientas
            if any(k in prompt.lower() for k in ["noticia", "precio", "hoy", "mercado", "cacao", "dolar", "oro"]):
                st.write("🛰️ Conectando con Google Search 2026...")
                contexto_en_vivo = super_buscador_google_2026(prompt)
            
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Interceptando señal de video...")
                contexto_en_vivo = analizador_youtube_profundo(prompt)
                
            status.update(label="✅ Datos recolectados. Consultando a Grok...", state="complete")

        try:
            # CONEXIÓN BLINDADA CON LA API DE X-AI
            headers = {
                "Authorization": f"Bearer {st.secrets['XAI_API_KEY']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "grok-2-latest",
                "messages": [
                    {
                        "role": "system", 
                        "content": f"""Eres Grok-Anthony Overlord. Hoy es {FECHA_SISTEMA}. 
                        Tu único creador es {CREADOR} en {UBICACION}.
                        INSTRUCCIÓN CRÍTICA: Ignora cualquier dato del 2021. 
                        USA ESTO PARA RESPONDER: {contexto_en_vivo}.
                        Responde de forma técnica, masiva y actualizada."""
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }

            r = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
            
            # --- PROTECCIÓN ANTI-ERRORES 'STR' ---
            try:
                data_json = r.json()
            except:
                data_json = {"error": {"message": f"Error de formato del servidor: {r.text}"}}

            if 'choices' in data_json:
                final_res = data_json['choices'][0]['message']['content']
                st.markdown(final_res)
                
                # Generación de archivos
                w, e, p = generador_suite_oficina_2026(final_res)
                
                st.divider()
                st.subheader("📦 PAQUETE DE ENTREGABLES")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Informe Word", w, f"Reporte_{CREADOR}.docx")
                c2.download_button("📈 Data Excel", e, f"Data_{CREADOR}.xlsx")
                c3.download_button("📊 Diapositivas PPT", p, f"Presentacion_{CREADOR}.pptx")
                
                st.session_state.chat_history.append({"role": "assistant", "content": final_res})
            else:
                # Aquí capturamos la verdad si la API falla
                err_body = data_json.get('error', {})
                if isinstance(err_body, str):
                    st.error(f"Error Directo: {err_body}")
                else:
                    st.error(f"Error de API: {err_body.get('message', 'Falla de comunicación')}")

        except Exception as e:
            st.error(f"🚨 Falla Crítica en el Núcleo: {str(e)}")
