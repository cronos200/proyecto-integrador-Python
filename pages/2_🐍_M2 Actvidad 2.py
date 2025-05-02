import streamlit as st
import pandas as pd
import io

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

def cargar_datos():
    return pd.read_csv("datasest/estudiantes_colombia.csv")

df = cargar_datos()

st.title("📊 Análisis de Estudiantes de Colombia")

# Primeras y últimas filas
col1, col2 = st.columns(2)
with col1:
    st.write("🧾 Primeras 5 filas:")
    st.dataframe(df.head())

with col2:
    st.write("🧾 Últimas 5 filas:")
    st.dataframe(df.tail())

# Sección info() y describe()
st.subheader("📌 Resumen del dataset")

with st.expander("ℹ️ Información general (info)"):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

with st.expander("📈 Estadísticas descriptivas (describe)"):
    st.dataframe(df.describe())

    st.subheader("🧮 Selecciona columnas para mostrar")

columnas = st.multiselect("Selecciona las columnas que quieres ver", df.columns.tolist(), default=["nombre", "edad", "promedio"])
st.dataframe(df[columnas])

# 4. Filtrar por promedio con slider
st.subheader("🎯 Filtrar estudiantes por promedio")

valor_promedio = st.slider("Selecciona un promedio mínimo", min_value=float(df["promedio"].min()), max_value=float(df["promedio"].max()), step=0.1, value=4.0)
df_filtrado = df[df["promedio"] > valor_promedio]

st.write(f"Mostrando estudiantes con promedio mayor a {valor_promedio}")
st.dataframe(df_filtrado)