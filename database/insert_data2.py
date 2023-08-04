import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

lista_personas = [
    ('rodrigo','espinoza','chavarria',35),
    ('estela','fueeny','sacnez',17),
    ('saul','carls','trueeli',27)
]

cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)", lista_personas)

conexion.commit()
conexion.close()