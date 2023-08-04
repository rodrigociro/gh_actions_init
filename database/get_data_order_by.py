import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS where edad > 18 ORDER BY EDAD ASC")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()