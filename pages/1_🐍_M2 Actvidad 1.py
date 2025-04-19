import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="🐍",
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
nombre = pd.Series(['luis', 'jhon', 'camilo', 'ana', 'sofia'])
edad = pd.Series([25,46,32,12,26])
colores_preferidos = (['rojo', 'azul', 'morado', 'amarillo', 'rosado'])

my_dataframe = pd.DataFrame({'Nombre': nombre, 'Edad': edad, 'Colores preferidos': colores_preferidos})

df = pd.DataFrame(my_dataframe)

print(df)
'''

st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

nombre = pd.Series(['luis', 'jhon', 'camilo', 'ana', 'sofia'])
edad = pd.Series([25,46,32,12,26])
colores_preferidos = (['rojo', 'azul', 'morado', 'amarillo', 'rosado'])

my_dataframe = pd.DataFrame({'Nombre': nombre, 'Edad': edad, 'Colores preferidos': colores_preferidos})
df = pd.DataFrame(my_dataframe)
st.dataframe(df)


st.header("Lista de diccionarios:")

codigo = """
datos = [{'Etnias en colombia': 'indijenas de colombia', 'Poblacion': 500, 'Pais': 'colombia'},
         {'Etnias en colombia': 'Afrocolombianos', 'Poblacion': 869, 'Pais': 'colombia'},
         {'Etnias en colombia': 'El pueblo rom', 'Poblacion': 143, 'Pais': 'colombia'}]

df = pd.DataFrame(datos)
st.text('Es un ejemplo son solo datos inventados')
st.dataframe(df)
"""

st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

datos = [{'Etnias en colombia': 'indijenas de colombia', 'Poblacion': 500, 'Pais': 'colombia'},
         {'Etnias en colombia': 'Afrocolombianos', 'Poblacion': 869, 'Pais': 'colombia'},
         {'Etnias en colombia': 'El pueblo rom', 'Poblacion': 143, 'Pais': 'colombia'}]

df = pd.DataFrame(datos)
st.text('Es un ejemplo son solo datos inventados')
st.dataframe(df)


st.header("Lista de listas:")

codigo = """
datos = [['Celulares', 50000,46],
         ['Maletas', 12000,100],
         ['Teclados', 2000,29]]

df = pd.DataFrame(datos, columns=['Producto', 'Precio', 'Cantidad'])
st.text('Productos en Inventario')
st.dataframe(df)
"""

st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

# nombre del producto, precio y cantidad en stock (usa datos inventados).
datos = [['Celulares', 50000,46],
         ['Maletas', 12000,100],
         ['Teclados', 2000,29]]

df = pd.DataFrame(datos, columns=['Producto', 'Precio', 'Cantidad'])
st.text('Productos en Inventario')
st.dataframe(df)


st.header('Series:')

codigo ="""
nombres = pd.Series(['Lina', 'Cristian', 'Mateo'])
edades = pd.Series([25,38,18])
ciudades = pd.Series(['Bogota', 'Medellin', 'Cartagena'])

df = pd.DataFrame({'Nombres': nombres, 'Edades': edades, 'Ciudades': ciudades})
st.text('Datos de Personas')
st.dataframe(df)
"""
st.subheader("📄 Código fuente:")
st.code(codigo, language='python')

# una con nombres de personas, otra con sus edades y otra con sus ciudades 
nombres = pd.Series(['Lina', 'Cristian', 'Mateo'])
edades = pd.Series([25,38,18])
ciudades = pd.Series(['Bogota', 'Medellin', 'Cartagena'])

df = pd.DataFrame({'Nombres': nombres, 'Edades': edades, 'Ciudades': ciudades})
st.text('Datos de Personas')
st.dataframe(df)



st.header('Archivo CSV (local):')

code = """
df = pd.read_csv('datasest/data.csv') El archivo es local para que te funcione pega la direccion de un archivo CSV de tu computadora 
st.text('Datos desde CSV')
st.dataframe(df)
"""

st.subheader("📄 Código fuente:")
st.code(code, language='python')

df = pd.read_csv('datasest/data.csv')
st.text('Datos desde CSV')
st.dataframe(df)


st.header('Archivo Excel (local):')

code = """
df = pd.read_excel('static/data.xlsx', engine='openpyxl') Archivo loca debes poner uno que se encuentre en tu computadara
st.text('Datos desde Excel')
st.dataframe(df)
"""
st.subheader('📄 Código fuente:')
st.code(code, language='python')

df = pd.read_excel('static/data.xlsx', engine='openpyxl')
st.text('Datos desde Excel')
st.dataframe(df)