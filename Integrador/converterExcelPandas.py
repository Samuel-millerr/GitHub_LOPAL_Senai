import pandas as pd

arquivo_csv = "arquivoCsv.csv"  # Atribui o arquivo .csv a uma variável do programa
df = pd.read_csv(arquivo_csv) # Realiza a leitura do arquivo .csv
df.to_excel("dadosAtualizados.xlsx", index = False) # Converte o csv para excel

