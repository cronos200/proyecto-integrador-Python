import streamlit as st
import pandas as pd
import sqlite3
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="🐍",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad, aprenderás a crear Series y DataFrames utilizando la biblioteca Pandas en Python. 
Exploraremos las diferentes maneras de construir estas estructuras de datos, así como sus aplicaciones prácticas en el análisis de datos.
Al finalizar, tendrás una comprensión sólida de cómo manejar y manipular datos utilizando Pandas.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Entender las estructuras de datos de Pandas
- Crear Series y DataFrames
- Manipular datos
- Realizar análisis básico de datos
- Aplicar conocimientos prácticos
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


st.header('Archivo JSON:')
code = """
df = pd.read_json('datasest/datos.json')
st.text('Datos de Usuarios desde JSON')
st.dataframe(df)
"""
st.subheader('📄 Código fuente:')
st.code(code, language='Python')

df = pd.read_json('datasest/datos.json')
st.text('Datos de Usuarios desde JSON')
st.dataframe(df)


st.header('URL:')
code = """
df = pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')
st.text('Datos desde URL')
st.dataframe(df)
"""

st.subheader('📄 Código fuente:')
st.code(code, language='python')

df = pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')
st.text('Datos desde URL')
st.dataframe(df)


st.header('Base de datos SQLite:')
code = """
conn = sqlite3.connect('estudiantes.db')    
df = pd.read_sql('SELECT * FROM estudiantes', conn)  
conn.close()  

st.title('Datos desde SQLite')
st.dataframe(df)
"""

st.subheader('📄 Código fuente:')
st.code(code, language='python')

conn = sqlite3.connect('estudiantes.db')    
df = pd.read_sql('SELECT * FROM estudiantes', conn)  
conn.close()  

st.title('Datos desde SQLite')
st.dataframe(df)


st.header('Array de NumPy:')
code = """
datos = np.array([['Moto', 5000000, '2026/02/12'],
                  ['Carro', 8000000, '2020/08/02'],
                  ['Avion', 15000000, '2015/12/30']])

df = pd.DataFrame(datos, columns=['Producto', 'Precio', 'Modelo'])
st.text('Datos desde NumPy')
st.dataframe(df)
"""
st.subheader('📄 Código fuente:')
st.code(code, language='python')

datos = np.array([['Moto', 5000000, '2026/02/12'],
                  ['Carro', 8000000, '2020/08/02'],
                  ['Avion', 15000000, '2015/12/30']])

df = pd.DataFrame(datos, columns=['Producto', 'Precio', 'Modelo'])
st.text('Datos desde NumPy')
st.dataframe(df)