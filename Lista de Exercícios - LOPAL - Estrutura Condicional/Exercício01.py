#EXERCÍCIO 01 - VERIFICADOR DE ANO BISSEXTO
ano = int(input("Insira o ano a ser verificado: "))

if ano <= 0:
    print("O ano escolhido é ou veio antes do ano 0. Por gentileza, tente novamente!")
elif ano % 4 == 0  and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
   print("O ano é bissexto!")

else:
   print("O ano não é bissexto!")
