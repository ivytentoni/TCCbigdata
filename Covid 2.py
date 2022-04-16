from sre_parse import State
import pandas as pd

dados = pd.read_csv(r'C:\Users\ivymo\OneDrive\Área de Trabalho\TCC\caso_full.csv')

dados_filtrados = dados['state']== 'TO'

print(dados[dados_filtrados])