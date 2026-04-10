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
st.set_page_config(page_title="GROK-ANTHONY TITÁN 2026", page_icon="🔱", layout="wide")

# --- VARIABLES DE ENTORNO ---
CREADOR = "Anthony Prado"
UBICACION = "Quinindé, Esmeraldas, Ecuador"
FECHA_SISTEMA = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# --- MÓDULOS DE INTELIGENCIA DE MERCADO ---

def buscador_profundo_2026(query):
    """Buscador de grado militar para datos de 2026"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        # Búsqueda específica de noticias y mercados
        r = requests.get(f"https://www.google.com/search?q={query}+2026+actualidad+ecuador", headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Extraemos bloques de noticias y fragmentos destacados
        noticias = []
        for g in soup.find_all('div', class_='BNeawe')[:8]:
            if len(g.get_text()) > 20:
                noticias.append(f"• {g.get_text()}")
        
        return "\n".join(noticias) if noticias else "No se hallaron datos frescos. Usando proyección algorítmica 2026."
    except Exception as e:
        return f"Error de rastreo: {str(e)}"

def inteligencia_youtube(url):
    """Escaneo y análisis de contenido audiovisual"""
    try:
        ydl_opts = {'quiet': True, 'skip_download': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            analisis = f"""
            DETALLES DEL VIDEO:
            - Título: {meta.get('title')}
            - Canal: {meta.get('uploader')}
            - Duración: {meta.get('duration')} seg
            - Descripción: {meta.get('description')[:800]}...
            """
            return analisis
    except:
        return "El sistema no pudo penetrar la seguridad del video de YouTube."

def crear_paquete_corporativo(texto_ia):
    """Generador masivo de entregables (Word, Excel, PPT)"""
    # 1. GENERAR WORD PROFESIONAL
    doc = Document()
    doc.add_heading(f'INFORME TÉCNICO - OPERADOR {CREADOR.upper()}', 0)
    doc.add_paragraph(f"Fecha de Emisión: {FECHA_SISTEMA}")
    doc.add_paragraph(f"Sede de Operaciones: {UBICACION}")
    doc.add_heading('Análisis y Conclusiones:', level=1)
    doc.add_paragraph(texto_ia)
    
    buf_word = io.BytesIO()
    doc.save(buf_word)
    
    # 2. GENERAR EXCEL DE DATOS
    df_data = pd.DataFrame({
        'Campo': ['Fecha', 'Operador', 'Estado', 'Sede', 'Versión'],
        'Valor': [FECHA_SISTEMA, CREADOR, 'Finalizado', UBICACION, 'Titan 2026']
    })
    buf_excel = io.BytesIO()
    with pd.ExcelWriter(buf_excel, engine='xlsxwriter') as writer:
        df_data.to_excel(writer, index=False, sheet_name='Data_Tecnica')
    
    # 3. GENERAR PRESENTACIÓN PPT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = f"REPORTE 2026 - {CREADOR}"
    slide.placeholders[1].text = f"Resultados del Análisis:\n{texto_ia[:700]}..."
    buf_ppt = io.BytesIO()
    prs.save(buf_ppt)
    
    return buf_word.getvalue(), buf_excel.getvalue(), buf_ppt.getvalue()

# --- INTERFAZ LATERAL (COMMAND CENTER) ---
with st.sidebar:
    st.title("🔱 COMMAND CENTER")
    st.subheader(f"Bienvenido, {CREADOR}")
    st.markdown(f"**Ubicación:** {UBICACION}")
    st.markdown(f"**Fecha:** {FECHA_SISTEMA}")
    st.divider()
    
    # Herramientas adicionales
    st.header("🛠️ Herramientas")
    archivo = st.file_uploader("📂 Cargar Base de Datos", type=["csv", "txt", "pdf"])
    if archivo:
        st.success("Archivo inyectado correctamente.")
        
    st.divider()
    if st.button("🚨 REINICIAR NÚCLEO"):
        st.session_state.chat_history = []
        st.rerun()

# --- CUERPO PRINCIPAL ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# --- LÓGICA DE PROCESAMIENTO ---
if prompt := st.chat_input("Escribe tu orden de nivel Overlord..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Notificaciones de estado
        with st.status("🛸 Activando protocolos de búsqueda 2026...") as status:
            contexto_en_vivo = ""
            
            # Detección de intención
            if any(k in prompt.lower() for k in ["precio", "noticia", "mercado", "clima", "hoy", "cacao", "dólar"]):
                st.write("🛰️ Rastreando satélites de Google...")
                contexto_en_vivo = buscador_profundo_2026(prompt)
            
            if "youtube.com" in prompt or "youtu.be" in prompt:
                st.write("📺 Escaneando video...")
                contexto_en_vivo = inteligencia_youtube(prompt)
                
            status.update(label="✅ Datos Recopilados. Consultando a Grok...", state="complete")

        try:
            # CONEXIÓN BLINDADA CON LA API
            headers = {
                "Authorization": f"Bearer {st.secrets['XAI_API_KEY']}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "grok-2-latest",
                "messages": [
                    {
                        "role": "system", 
                        "content": f"""Eres Grok-Anthony Titán. Hoy es Abril de 2026. 
                        Tu creador es {CREADOR}. Operas desde {UBICACION}.
                        PROHIBIDO: Usar datos de 2021 o anteriores. 
                        USA ESTO: {contexto_en_vivo}.
                        ESTILO: Técnico, potente, directo y muy actualizado."""
                    },
                    {"role": "user", "content": prompt}
                ]
            }

            r = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
            
            # Traductor de errores para evitar el fallo 'str'
            try:
                data_json = r.json()
            except:
                data_json = {"error": {"message": f"Respuesta corrupta: {r.text}"}}

            if 'choices' in data_json:
                final_text = data_json['choices'][0]['message']['content']
                st.markdown(final_text)
                
                # GENERACIÓN DE ENTREGABLES
                w, e, p = crear_paquete_corporativo(final_text)
                
                st.divider()
                st.subheader("📦 PAQUETE DE ENTREGABLES GENERADO")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Informe Word", w, f"Reporte_{CREADOR}.docx")
                c2.download_button("📈 Data Excel", e, f"Analisis_{CREADOR}.xlsx")
                c3.download_button("📊 Diapositivas PPT", p, f"Presentacion_{CREADOR}.pptx")
                
                st.session_state.chat_history.append({"role": "assistant", "content": final_text})
            else:
                error_api = data_json.get('error', {})
                st.error(f"⚠️ Error detectado: {error_api.get('message', 'Falla de comunicación')}")

        except Exception as e:
            st.error(f"🚨 Error Crítico en el Núcleo: {str(e)}")
