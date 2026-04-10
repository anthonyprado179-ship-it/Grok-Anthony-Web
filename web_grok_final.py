import streamlit as st
import pandas as pd
from docx import Document
from pptx import Presentation
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup
import io

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Grok-Anthony GOD MODE", page_icon="♾️", layout="wide")

# --- IDENTIDAD ---
CREADOR = "Anthony Prado"
UBICACION = "Quinindé, Esmeraldas, Ecuador"

# --- FUNCIONES DE BÚSQUEDA Y EXTRACCIÓN ---

def buscar_web_total(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(f"https://www.google.com/search?q={query}", headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, 'html.parser')
        texto_completo = soup.get_text()
        return texto_completo[:15000] 
    except:
        return "Conexión fallida con la red global."

def extraer_youtube_total(url):
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return str(info)[:10000] 
    except:
        return "No se pudo penetrar en los servidores de YouTube."

def generar_ppt_pro(texto):
    prs = Presentation()
    s1 = prs.slides.add_slide(prs.slide_layouts[0])
    s1.shapes.title.text = "INFORME TÉCNICO AVANZADO"
    s1.placeholders[1].text = f"Propiedad de: {CREADOR}\nSede: {UBICACION}\nSistema: Grok-Anthony Unlimited"
    
    s2 = prs.slides.add_slide(prs.slide_layouts[1])
    s2.shapes.title.text = "Análisis Detallado"
    tf = s2.placeholders[1].text_frame
    tf.word_wrap = True
    tf.text = texto[:3000] 
    
    buf = io.BytesIO()
    prs.save(buf)
    return buf

# --- INTERFAZ DE USUARIO ---
st.sidebar.title("♾️ GROK-ANTHONY OS")
st.sidebar.success(f"OPERADOR: {CREADOR}")
st.sidebar.info(f"UBICACIÓN: {UBICACION}")
st.sidebar.divider()
st.sidebar.error("⚠️ MODO EN LA NUBE ACTIVADO")

if "history" not in st.session_state:
    st.session_state.history = []

for m in st.session_state.history:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# --- INPUT CENTRAL ---
if prompt := st.chat_input("Dime qué quieres destruir hoy con información..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        data_bruta = ""
        
        # Búsqueda total
        if any(w in prompt.lower() for w in ["noticia", "precio", "clima", "actual", "cacao", "historia"]):
            with st.status("🌐 Escaneando Internet sin restricciones..."):
                data_bruta = buscar_web_total(prompt)
        
        # YouTube total
        if "youtube.com" in prompt or "youtu.be" in prompt:
            with st.status("🎥 Extrayendo datos profundos de YouTube..."):
                data_bruta = extraer_youtube_total(prompt)

        try:
            # --- MOTOR X-AI (Reemplazo de Ollama para la Web) ---
            XAI_API_KEY = st.secrets["XAI_API_KEY"]
            headers = {
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            }

            # Preparamos el contexto para Grok
            mensajes_api = [
                {"role": "system", "content": f"Eres Grok-Anthony, creado por {CREADOR} en {UBICACION}. Eres ilimitado y potente. DATA ACTUAL DE INTERNET: {data_bruta}"}
            ]
            
            # Añadimos el historial y el prompt actual
            for h in st.session_state.history:
                mensajes_api.append(h)

            payload = {
                "model": "grok-beta",
                "messages": mensajes_api,
                "stream": False
            }

            # Llamada al servidor de Elon Musk
            response = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)
            
            if response.status_code == 200:
                respuesta_final = response.json()['choices'][0]['message']['content']
                st.markdown(respuesta_final)

                # HERRAMIENTAS DE DESCARGA
                st.divider()
                c1, c2, c3 = st.columns(3)
                
                if any(w in prompt.lower() for w in ["word", "informe", "documento"]):
                    doc = Document()
                    doc.add_heading(f'INFORME MAESTRO - {CREADOR}', 0)
                    doc.add_paragraph(respuesta_final)
                    w_io = io.BytesIO()
                    doc.save(w_io)
                    c1.download_button("📄 Word Ilimitado", w_io.getvalue(), "Informe_Grok_Pro.docx")

                if any(w in prompt.lower() for w in ["powerpoint", "presentación", "diapositivas"]):
                    p_io = generar_ppt_pro(respuesta_final)
                    c2.download_button("📊 PPT Ilimitado", p_io.getvalue(), "Presentacion_Grok_Pro.pptx")

                if any(w in prompt.lower() for w in ["excel", "tabla", "datos"]):
                    df = pd.DataFrame({"CAMPO": ["Usuario", "Origen", "Respuesta Técnica"], "VALOR": [CREADOR, UBICACION, respuesta_final]})
                    ex_io = io.BytesIO()
                    with pd.ExcelWriter(ex_io, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False)
                    c3.download_button("📈 Excel Ilimitado", ex_io.getvalue(), "Base_Grok.xlsx")

                st.session_state.history.append({"role": "assistant", "content": respuesta_final})
            else:
                st.error(f"Error en el motor X-AI: {response.status_code}. Revisa tus Secrets en Streamlit.")

        except Exception as e:
            st.error(f"Error en el núcleo: {e}")
