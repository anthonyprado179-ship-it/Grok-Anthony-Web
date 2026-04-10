import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# --- CONFIGURACIÓN ESTRATÉGICA ---
st.set_page_config(
    page_title="TITÁN SUPREMO 2026", 
    page_icon="🔱", 
    layout="wide"
)

# IDENTIDAD DEL OPERADOR
CREADOR = "Anthony Prado"
UBICACION = "Quinindé, Esmeraldas, Ecuador"

# --- CONEXIÓN CON SETTINGS (SECRETS) ---
try:
    # Aquí llamamos a la llave que configuraste en Settings
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("🚨 ERROR: No se encontró la API KEY en los Secrets de Streamlit.")
    st.stop()

# --- NÚCLEO DE RASTREO 2026 (DATOS ACTUALIZADOS) ---
def rastreador_tiempo_real(query):
    """Escanea la red buscando datos de abril 2026 en Ecuador"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        # Forzamos la búsqueda a la fecha actual en Quinindé
        url = f"https://www.google.com/search?q={query}+Ecuador+abril+2026+precios+noticias"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        resultados = []
        for item in soup.find_all(['h3', 'span']):
            texto = item.get_text().strip()
            if len(texto) > 65:
                resultados.append(f"📡 SEÑAL 2026: {texto}")
        return "\n".join(resultados[:10])
    except:
        return "Sincronización externa en espera. Usando base de datos interna."

# --- INTERFAZ SIDEBAR ---
with st.sidebar:
    st.title("🔱 NÚCLEO TITÁN")
    st.markdown("---")
    st.success(f"👤 OPERADOR: {CREADOR}")
    st.info(f"📍 SEDE: {UBICACION}")
    st.write(f"📅 HOY: {datetime.now().strftime('%d/%m/%Y')}")
    if st.button("🚨 PURGAR MEMORIA"):
        st.session_state.chat_history = []
        st.rerun()

# --- MEMORIA DEL SISTEMA ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- PROCESAMIENTO DE ÓRDENES ---
if prompt := st.chat_input("Inserta tus comandos, Anthony..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🛸 Analizando datos de 2026...") as status:
            # 1. Obtener datos frescos de internet
            contexto_2026 = rastreador_tiempo_real(prompt)
            
            try:
                # 2. Generar respuesta con el modelo más potente
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                sistema_prompt = f"""
                Eres la Inteligencia Suprema de {CREADOR}. 
                Tu base de operaciones es {UBICACION}. 
                Estamos en ABRIL DE 2026. 
                
                DATOS ACTUALES DETECTADOS:
                {contexto_2026}
                
                INSTRUCCIÓN: Proporciona un análisis técnico masivo, detallado y con datos del 2026.
                """
                
                respuesta = model.generate_content(f"{sistema_prompt}\n\nORDEN DEL OPERADOR: {prompt}")
                texto_final = respuesta.text
                status.update(label="✅ Inteligencia Generada", state="complete")
            except Exception as e:
                texto_final = f"Falla en el núcleo: {str(e)}"
                status.update(label="❌ Error de conexión", state="error")

        st.markdown(texto_final)
        st.session_state.chat_history.append({"role": "assistant", "content": texto_final})
