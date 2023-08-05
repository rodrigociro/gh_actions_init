import pandas as pd
import numpy as np

valores=range(4)
indices=list('CABD')
serie = pd.Series(valores,index=indices)
print(serie)
print(serie.sort_index())
print(serie.rank())


serie2=pd.Series(np.random.rand(10))
print(serie2)
print(serie2.rank())
print(serie2.sort_values())