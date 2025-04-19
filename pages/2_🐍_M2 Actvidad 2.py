import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="🐍",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

st.header("Solución Activiada #2")

df = pd.read_csv("datasest/estudiantes_colombia.csv")
st.dataframe(df)
st.header("Ver las 5 filas y las ultimas 5 filas del dataframe")
st.subheader("¿como se hizo?")

codigo = """
df = pd.read_csv("datasest/estudiantes_colombia.csv")
st.write(df.head()) Primera 5 filas
st.write(df.tail()) Ultimas 5 filas
"""
st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

st.subheader("Primera 5 filas")
st.write(df.head())
st.subheader("Ultimas 5 filas")
st.write(df.tail())

