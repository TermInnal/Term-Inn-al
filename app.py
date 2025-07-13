import streamlit as st
import subprocess

st.set_page_config(page_title="Term-Inn-al", layout="centered")
st.title("Term-Inn-al")

try:
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    st.text(result.stdout)
except Exception as e:
    st.error(f"Erro ao executar o jogo: {e}")