import pandas as pd
import webbrowser

website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)

dataframe_nba = pd.read_clipboard()