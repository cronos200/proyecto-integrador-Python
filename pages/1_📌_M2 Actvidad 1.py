import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

st.header("Solución de la actividad #1")

st.subheader('Diccionario:')

codigo = '''
import pandas as pd

datos = [{"Nombre": "Ana", "Edad": 25, "Ciudad": "Madrid"},
         {"Nombre": "Juan", "Edad": 30, "Ciudad": "Barcelona"},
         {"Nombre": "Pedro", "Edad": 35, "Ciudad": "Sevilla"}]

df = pd.DataFrame(datos)

print(df)
'''

st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

datos = [{"Nombre": "Ana", "Edad": 25, "Ciudad": "Madrid"},
         {"Nombre": "Juan", "Edad": 30, "Ciudad": "Barcelona"},
         {"Nombre": "Pedro", "Edad": 35, "Ciudad": "Sevilla"}]

df = pd.DataFrame(datos)

st.dataframe(df)



