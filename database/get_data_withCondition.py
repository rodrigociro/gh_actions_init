import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

nombre = [
    "rodrigo"
]

cursor.execute("SELECT * FROM PERSONAS WHERE nombre = ?", nombre)

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()