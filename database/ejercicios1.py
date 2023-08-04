import sqlite3

#crear base de datos, producto, 3 campos.
conexion = sqlite3.connect("basededatos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")
conexion.commit()
conexion.close()


#datos a insertar
insertar = [
    (1,"Impresora",300),
    (2,"Raton",20),
    (3,"Ordenador",600)
]

conexion2 = sqlite3.connect("basededatos.db")
cursor2 = conexion2.cursor()
cursor2.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",insertar)
conexion2.commit()
conexion2.close()

conexion3 = sqlite3.connect("basededatos.db")
cursor3 = conexion3.cursor()
cursor3.execute("SELECT * FROM PRODUCTOS")
amigo=cursor3.fetchall()
for a in amigo:
    print(a)
conexion3.close()