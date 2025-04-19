import streamlit as st
import pandas as pd
import faker

# Configuración de la página
st.set_page_config(   
    page_icon="🐍",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.title("Accede a mi notebook en Google Colab")

st.write("Puedes ver el código y ejecutarlo en este enlace:")
st.markdown("[👉 Abrir en Google Colab](https://colab.research.google.com/drive/1gZgKSP1CeglxKAlv7rsyOtL9LDIMSk5Y)")

