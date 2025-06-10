import pandas as pd
#
# historico_pedidos = [
# {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},
# {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},
# {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},
# {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
# ]
#
# workbook = openpyxl.Workbook()
# sheet = workbook.active
# sheet.append(["ID", "Nome", "Endereço", "Produto", "Quantidade", "Preço", "Data"])
#
# for pedido in historico_pedidos:
#     sheet.append([pedido["ID"], pedido["Nome"], pedido["Endereço"], pedido["Produto"], pedido["Quantidade"], pedido["Preço"], pedido["Data"]])
#
# workbook.save("exercicio01Dados.xlsx")

historico_pedidos = [
{'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},
{'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},
{'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},
{'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
]

df = pd.DataFrame(historico_pedidos)
df.to_excel("dados.xlsx", index = False)
