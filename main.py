import streamlit as st
from streamlit_pages import ordenamiento
from streamlit_pages import backtracking
from streamlit_pages import voraces


# Inicializar estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "ordenamiento"

# Barra de menú con columnas
col1, col2, col3 = st.columns(3)

if col1.button("🔢 Ordenamiento"):
    st.session_state.pagina = "ordenamiento"
if col2.button("🔙 Backtracking"):
    st.session_state.pagina = "backtracking"
if col3.button("🦁 Voraces"):
    st.session_state.pagina = "voraces"

# Mostrar la página activa
if st.session_state.pagina == "ordenamiento":
    ordenamiento()
elif st.session_state.pagina == "backtracking":
    backtracking()
elif st.session_state.pagina == "voraces":
    voraces()
