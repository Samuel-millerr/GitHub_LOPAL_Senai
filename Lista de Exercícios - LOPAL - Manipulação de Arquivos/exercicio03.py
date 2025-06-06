import pandas as pd

df = pd.read_csv("exercicio02Dados.csv")
df.to_json("exercicio03Dados.json", indent=4)