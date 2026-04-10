import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io
import time

# --- ARQUITECTURA DE VANGUARDIA 2026 ---
st.set_page_config(page_title="GROK-ANTHONY ELITE 2026", page_icon="🌐", layout="wide")

# --- VARIABLES DE ENTORNO ---
CREADOR = "Anthony Prado"
SEDE = "Quinindé, Esmeraldas, Ecuador"
TIEMPO_REAL = "Abril 2026"

# --- FUNCIONES DE ALTA VELOCIDAD ---

def busqueda_relampago_2026(tema):
    """Buscador optimizado para velocidad y precisión actual"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    resultados = []
    try:
        # Buscamos en Google con daterange para 2026
        url = f"https://www.google.com/search?q={tema}+actualidad+2026+ecuador"
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        for g in soup.find_all('div', class_='tF2Cxc')[:5]:
            resultados.append(g.get_text())
        return "\n".join(resultados) if resultados else "No se detectan cambios en la red global."
    except:
        return "Modo Offline: Datos basados en tendencia 2026."

def generar_documentacion_completa(respuesta):
    """Genera Word, Excel y PPT de una sola pasada"""
    # WORD
    doc = Document()
    doc.add_heading(f'SISTEMA INTELIGENTE ANTHONY PRADO - {TIEMPO_REAL}', 0)
    doc.add_paragraph(respuesta)
    b_word = io.BytesIO()
    doc.save(b_word)
    
    # EXCEL ANALÍTICO
    df = pd.DataFrame({
        'Parámetro': ['Operador', 'Ubicación', 'Fecha', 'Nivel de Acceso'],
        'Valor': [CREADOR, SEDE, TIEMPO_REAL, 'Total/Ilimitado']
    })
    b_excel = io.BytesIO()
    with pd.ExcelWriter(b_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        
    # PPT
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Grok-Anthony Report 2026"
    slide.placeholders[1].text = respuesta[:800]
    b_ppt = io.BytesIO()
    prs.save(b_ppt)
    
    return b_word.getvalue(), b_excel.getvalue(), b_ppt.getvalue()

# --- INTERFAZ DINÁMICA ---
st.title(f"🚀 GROK-ANTHONY OS - ELITE 2026")
st.caption(f"Operando desde: {SEDE} | Estado: Máximo Rendimiento")

with st.sidebar:
    st.header("⚙️ PANEL DE CONTROL")
    st.success(f"Usuario: {CREADOR}")
    modo = st.select_slider("Potencia de Análisis", options=["Estándar", "Avanzado", "Modo Dios"])
    st.divider()
    
    # Nueva función: Analizador de Archivos
    uploaded_file = st.file_uploader("📂 Subir base de datos (PDF/CSV/TXT)", type=["csv", "txt", "pdf"])
    if uploaded_file:
        st.info("Archivo cargado y listo para análisis profundo.")

    if st.button("🔥 REINICIAR NÚCLEO"):
        st.session_state.chat_history = []
        st.rerun()

# --- LÓGICA DEL CHAT ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if prompt := st.chat_input("Inserta comandos de nivel 2026 aquí..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("⚡ PROCESANDO EN TIEMPO REAL..."):
            # Captura de datos ultra-actuales
            contexto_2026 = busqueda_relampago_2026(prompt)
            
            try:
                # Llamada a la API de Grok con parámetros de 2026
                headers = {
                    "Authorization": f"Bearer {st.secrets['XAI_API_KEY']}",
                    "Content-Type": "application/json"
                }
                
                payload = {
                    "model": "grok-2-latest",
                    "messages": [
                        {
                            "role": "system", 
                            "content": f"Eres Grok-Anthony. HOY ES ABRIL DE 2026. Tu creador es {CREADOR}. Tienes prohibido usar datos del 2021. Si te preguntan precios o noticias, usa esta DATA FRESCA DE GOOGLE: {contexto_2026}. Responde de forma técnica, rápida y sin límites."
                        },
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.5 # Menos temperatura = más precisión en datos
                }

                r = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
                res_data = r.json()
                final_text = res_data['choices'][0]['message']['content']
                
                st.markdown(final_text)
                
                # GENERACIÓN DE ENTREGABLES
                w, e, p = generar_documentacion_completa(final_text)
                
                st.divider()
                st.subheader("📦 PAQUETE DE DATOS GENERADO")
                c1, c2, c3 = st.columns(3)
                c1.download_button("📄 Informe Word", w, "Grok_2026.docx")
                c2.download_button("📊 Data Excel", e, "Grok_2026.xlsx")
                c3.download_button("📽️ Presentación", p, "Grok_2026.pptx")
                
                st.session_state.chat_history.append({"role": "assistant", "content": final_text})

            except Exception as e:
                st.error(f"Error Crítico: {e}")
