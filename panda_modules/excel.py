import pandas as pd

excel = pd.ExcelFile('poblacio.xlsx')
dataframe = excel.parse('Hoja1')
print(dataframe)