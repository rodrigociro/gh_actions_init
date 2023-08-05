import pandas as pd
import numpy as np

dataframe_nba = pd.read_clipboard()
print(dataframe_nba)

print(dataframe_nba.columns)

print(dataframe_nba['Continente'])

print(dataframe_nba.loc[0])

print(dataframe_nba.loc[0:3],['Continente',['Población']])