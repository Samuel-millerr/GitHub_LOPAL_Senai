# import csv
#
# with open("meu_arquivo.csv","w", newline='') as arquivo:
#     csv.writer(arquivo).writerow(["Nome,Preço"])
#     csv.writer(arquivo).writerow(["Livro,20"])
#
# with open("meu_arquivo.csv","r") as arquivo:
#     for i in csv.reader(arquivo):
#         print(i)
#

# import json
#
# dados = {
#     "Nome": "Samuel",
#     "Idade": "18 anos",
#     "Cidade": "Campinas"
# }
#
# with open("teste.json","w") as arquivo:
#     json.dump(dados, arquivo)
#
# with open("teste.json","r") as arquivo:
#     arquivo = json.load(arquivo)
#     for chave, valor in arquivo.items():
#         print(f"{chave}: {valor}")

# xml_str = """<config>
#     <versao>1.1</versao>
# </config>"""
# with open ("config.xml","w") as arquivo:
#     arquivo.write(xml_str)
#
# with open ("config.xml","r") as arquivo:
#     print(arquivo.read())

import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(['Produto','Valor'])
sheet.append(['Celular','10'])

workbook.save("teste.xlsx")

for row in sheet.iter_rows(min_row=0, values_only = True):
    print(row)

