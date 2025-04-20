import sqlite3  

# Crear/Conectar a la base de datos  
conn = sqlite3.connect('estudiantes.db')  
cursor = conn.cursor()  

# Crear tabla  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS estudiantes (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    nombre TEXT NOT NULL,  
    calificacion INTEGER NOT NULL  
)  
''')  

# Insertar datos  
estudiantes = [  
    ('Alice', 90),  
    ('Bob', 75),  
    ('Charlie', 85)  
]  

cursor.executemany('INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)', estudiantes)  

# Guardar cambios y cerrar la conexión  
conn.commit()  
conn.close()  