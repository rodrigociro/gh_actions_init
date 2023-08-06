import pandas as pd
import webbrowser

url = "https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol"
dataframe = pd.io.html.read_html(url)
print(dataframe)
dataframe_futbol = dataframe[0]
print(dataframe_futbol)
print(dataframe_futbol.loc[0])