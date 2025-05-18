import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="🐍",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

st.header("Solución de la actividad 4")

df = pd.read_csv('static/Fleet Data.csv')
st.subheader('✈️ Flotas de aerolíneas✈️ ')
st.text('Planespotters.net tiene una base de datos completa sobre las aerolíneas de todo el mundo y los aviones que cada uno posee y opera.Este conjunto de datos recopila las 100+ principales aerolíneas del mundo (por el tamaño de su flota). Se combina con la información que se encuentra en Wikipedia sobre la flota de la aerolínea respectiva y el valor/costo promedio del avión fabricado.')
st.dataframe(df)
df.set_index('Aerolínea', inplace=True)

st.subheader('Algunos datos de la aerolinea Aeroflot utilizando el metodo .loc')
code = """
st.write(df.loc['Aeroflot',['En operación (actual)','Tipo de aeronave','Históricas (retiradas)']])
"""
st.subheader('🔎Codigo')
st.code(code, language='python')
st.write(df.loc['Aeroflot',['En operación (actual)','Tipo de aeronave','Históricas (retiradas)']])


st.subheader('Algunos datos de la aerolinea Aire france  utilizando el metodo .iloc')
code = """
st.write(df.iloc[180,[2,5]])
"""
st.subheader('🔎codigo')
st.code(code, language='Python')
st.write(df.iloc[180,[2,5]])



