import csv
import openpyxl

with open("arquivoCsv.csv", "r") as arquivo: # Abre o arquivo .csv
    reader = csv.DictReader(arquivo) # Realiza a leitura do mesmo
    datas = []
    for i in reader: # Estrutura os dados das linhas em um dicionário
        dadosData = {
            "Data": i["Date"],
            "Horário": i['Time'],
            "Esteira01": i["esteira1"],
            "Esteira02": i["esteira2"],
            "Esteira03": i["esteira3"]
        }
        datas.append(dadosData) # Adiciona as informações das linhas em uma lista

# Criação da planilha no Excel através da biblioteca "openpyxl"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["Data", "Horário", "Esteira01", "Esteira02", "Esteira03"]) # Adiciona o cabeçalho na planilha

for data in datas: # O for percorre a lista com as informações das linhas, adicionando cada uma em sua respectiva coluna
    sheet.append([data["Data"], data["Horário"], data["Esteira01"], data["Esteira02"], data["Esteira03"]])

workbook.save("dadosAtualizados.xlsx")
