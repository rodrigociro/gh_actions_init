import pandas as pd
import webbrowser

url = "https://es.wikipedia.org/wiki/Copa_Mundial_de_Fútbol"
dataframe=pd.io.html.read_html(url)
print(dataframe)