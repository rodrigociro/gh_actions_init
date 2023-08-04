import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES('Antonio','Perez','Segundo Apellido',35)")

conexion.commit()
conexion.close()