import pywhatkit as py
import csv

# Função para definir o emoji de acordo com o valor do estoque
def emoji(valor):
    legenda = {
        "0": "⚪",
        "1": "🔴",
        "2": "🟡",
        "3": "🟢"
    }
    return legenda.get(valor)

# Função para ler arquivo .csv, utilizada nos exercícios anteriores
def ler_csv(arquivo_csv):
    with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for indice, linha in enumerate(reader):
            if indice == 1: # Verifica a primeira linha do arquivo csv (ultima data adicionada)
                dados_dia = linha

    dados = f"Estoque em {dados_dia[0]}: Esteira01: {emoji(dados_dia[2])} {dados_dia[2]} | Esteira02: {emoji(dados_dia[3])} {dados_dia[3]} | Esteira03: {emoji(dados_dia[4])} {dados_dia[4]}\n"
    return dados

dados = ler_csv("arquivoCsv.csv") # Chamada da função com o parametro sendo o arquivo .csv
informacoes = f"Olá, segue a baixo o relatório do dia: \n{dados}" # Estruturação da mensagem para ser enviada no whatsapp

py.sendwhatmsg_instantly("+55 19 999720938", informacoes) # Envio da mensagem por whatsapp