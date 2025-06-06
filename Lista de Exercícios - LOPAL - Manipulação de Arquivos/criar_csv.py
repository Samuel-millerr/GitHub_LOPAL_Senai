import csv

with open("meu_arquivo.csv","w", newline='') as arquivo:
    csv.writer(arquivo).writerow(["Nome,Preço"])
    csv.writer(arquivo).writerow(["Livro,20"])

with open("meu_arquivo.csv","r") as arquivo:
    for i in csv.reader(arquivo):
        print(i)
