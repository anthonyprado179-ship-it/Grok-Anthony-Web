import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io
import time

# --- ARQUITECTURA ELITE 2026 ---
st.set_page_config(page_title="GROK-ANTHONY OVERLORD", page_icon="⚡", layout="wide")

# --- IDENTIDAD ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
VERSION = "6.0 - 2026 Edition"

# --- FUNCIONES DE ALTO IMPACTO ---

def buscar_mercados_vivos(query):
    """Buscador optimizado para precios y noticias frescas 2026"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        url = f"https://www.google.com/search?q={query}+precio+hoy+2026"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        noticias = [n.get_text() for n in soup.find_all('div', class_='BNeawe')[:5]]
        return "\n".join(noticias)
    except:
        return "Conexión limitada. Usando proyecciones 2026."

def procesar_video_ia(url):
    """Escaneo profundo de contenido de YouTube"""
    try:
        with YoutubeDL({'quiet': True, 'skip_download': True}) as ydl:
            meta = ydl.extract_info(url, download=False)
            return f"Título: {meta['title']}\nVistas: {meta['view_count']}\nResumen: {meta['description'][:500]}"
    except:
        return "Video no accesible por restricciones de red."

def exportar_todo(texto):
    """Generación de suite de oficina instantánea"""
    # WORD
    doc = Document()
    doc.add_heading(f'INFORME ESTRATÉGICO - {CREADOR}', 0)
    doc.add_paragraph(texto)
    f_word = io.BytesIO()
    doc.save(f_word)
    
    # EXCEL
    df = pd.DataFrame({"METRICA": ["Analista", "Año", "Estado"], "VALOR": [CREADOR, "2026", "ACTIVO"]})
    f_excel = io.BytesIO()
    with pd.ExcelWriter(f_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        
    # PPT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "ANÁLISIS DE DATOS 2026"
    slide.placeholders[1].text = texto[:1000]
    f_ppt = io.BytesIO()
    prs.save(f_ppt)
    
    return f_word.getvalue(), f_excel.getvalue(), f_ppt.getvalue()

# --- INTERFAZ DINÁMICA ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100)
    st.title("SISTEMA OVERLORD")
    st.success(f"OPERADOR: {CREADOR}")
    st.info(f"UBICACIÓN: {SEDE}")
    st.divider()
    
    archivo = st.file_uploader("📂 Inyectar Datos (PDF/CSV/TXT)", type=["txt", "csv", "pdf"])
    
    if st.button("🗑️ LIMPIAR NÚCLEO"):
        st.session_state.history = []
        st.rerun()

# --- LÓGICA DEL CHAT ---
if "history" not in st.session_state:
    st.session_state.history = []

for m in st.session_state.history:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Dime qué quieres dominar hoy..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Extrayendo datos del 2026..."):
            # Lógica de búsqueda automática
            contexto = ""
            if any(k in prompt.lower() for k in ["precio", "noticia", "hoy", "cacao", "oro"]):
                contexto = buscar_mercados_vivos(prompt)
            if "youtube.com" in prompt or "youtu.be" in prompt:
                contexto = procesar_video_ia(prompt)

        try:
            # CONEXIÓN CON GROK (Usando tu nueva API Key de los Secrets)
            headers = {
                "Authorization": f"Bearer {st.secrets['XAI_API_KEY']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "grok-2-latest",
                "messages": [
                    {
                        "role": "system", 
                        "content": f"Eres Grok-Anthony Overlord. HOY ES ABRIL DE 2026. Creador: {CREADOR}. SEDE: {SEDE}. USA ESTOS DATOS EN TIEMPO REAL: {contexto}. Eres el sistema más rápido del mundo."
                    },
                    {"role": "user", "content": prompt}
                ]
            }

            r = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
            data = r.json()

            if 'choices' in data:
                res_final = data['choices'][0]['message']['content']
                st.markdown(res_final)
                
                # GENERAR ARCHIVOS
                w, e, p = exportar_todo(res_final)
                st.divider()
                st.subheader("📦 PAQUETE DE ENTREGABLES")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Informe Word", w, "Reporte_2026.docx")
                c2.download_button("📈 Hoja Excel", e, "Datos_2026.xlsx")
                c3.download_button("📊 Diapositivas", p, "Presentacion_2026.pptx")
                
                st.session_state.history.append({"role": "assistant", "content": res_final})
            else:
                st.error(f"Error en la API: {data.get('error', {}).get('message', 'Llave inválida')}")

        except Exception as err:
            st.error(f"Falla en el Núcleo: {err}")
