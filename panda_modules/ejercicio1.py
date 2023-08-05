import pandas as pd
import numpy as np

minimo=10
maximo=40
veces=3
alumnos = np.random.randint(minimo,maximo,veces)
print(alumnos)

clases = ['clase1','clase2','clase3']
clases1 = pd.Series(alumnos,index=clases)
print(clases1)