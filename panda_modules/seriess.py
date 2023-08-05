#series
import pandas as pd
serie1 = pd.Series([3,5,7])
print(serie1)

asignaturas = ["matematicas","historia","fisica","literatura"]
notas = [8,6,9,7]
serie2 = pd.Series(notas,index=asignaturas)
print(serie2)
print(serie2["fisica"])
print(serie2[serie2 >= 8])

serie2.index.name = "notas de daniel"
serie2.name ="notas"
print("================")
print(serie2)

diccionar = serie2.to_dict()
print(diccionar)

serie3 = pd.Series(diccionar)
print(serie3)

