#generar ficheros de texto desde python

fichero = open("fichero_creado.txt","wt")

texto_de_fichero = """
rddas
dsadasd
das
"""
fichero.write(texto_de_fichero)

fichero.close()