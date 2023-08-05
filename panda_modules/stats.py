import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])

dataframe = pd.DataFrame(array,index=list('ab'),columns=list('123'))
print(dataframe)
print(dataframe.sum())

print(dataframe.sum(axis=1))
print(dataframe.min())
print("==========")
print(dataframe.idxmin())
print("==========")
print(dataframe.describe())