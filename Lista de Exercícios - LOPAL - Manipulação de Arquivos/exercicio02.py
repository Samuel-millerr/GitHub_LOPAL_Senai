import pandas as pd

arquivo_xlsx = "exercicio01Dados.xlsx"
df = pd.read_excel(arquivo_xlsx)
df.to_csv("exercicio02Dados.csv", index=False, encoding="utf-8")