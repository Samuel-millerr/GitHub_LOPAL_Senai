import json

dados = {
    "Nome": "Samuel",
    "Idade": "18 anos",
    "Cidade": "Campinas"
}

with open("meu_arquivo.json","w") as arquivo:
    json.dump(dados, arquivo)

with open("teste.json","r") as arquivo:
    arquivo = json.load(arquivo)
    for chave, valor in arquivo.items():
        print(f"{chave}: {valor}")