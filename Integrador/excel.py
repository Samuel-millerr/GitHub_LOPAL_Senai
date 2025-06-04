import csv
import openpyxl
import pandas as pd

# Primeira Forma
# with open("arquivoCsv.csv", "r") as arquivo:
#     reader = csv.DictReader(arquivo)
#     datas = []
#     for i in reader:
#         dadosData = {
#             "Data": i["Date"],
#             "Horário": i['Time'],
#             "Esteira01": i["esteira1"],
#             "Esteira02": i["esteira2"],
#             "Esteira03": i["esteira3"]
#         }
#         datas.append(dadosData)
#
# workbook = openpyxl.Workbook()
# sheet = workbook.active
# sheet.append(["Data", "Horário", "Esteira01", "Esteira02", "Esteira03"])
#
# for data in datas:
#     sheet.append([data["Data"], data["Horário"], data["Esteira01"], data["Esteira02"], data["Esteira03"]])
#
# workbook.save("dadosAtualizados.xlsx")

#Segunda Forma
arquivo_csv = "arquivoCsv.csv"
df = pd.read_csv(arquivo_csv)
df.to_excel("dadosAtualizados.xlsx", index = False)

