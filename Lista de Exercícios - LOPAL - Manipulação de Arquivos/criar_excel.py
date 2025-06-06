import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(['Produto','Valor'])
sheet.append(['Celular','10'])

workbook.save("meu_arquivo.xlsx")

for row in sheet.iter_rows(min_row=0, values_only = True):
    print(row)

