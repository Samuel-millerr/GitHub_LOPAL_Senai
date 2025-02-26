#EXERCÍCIO 05 - VERIFICAÇÃO DE PARES
#PEDE OS NÚMEROS AO USUÁRIO
numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

#CALCULO SE É IMPAR OU PAR
resto_numero01 = numero01 % 2
resto_numero02 = numero02 % 2

#IMPRESSÃO DO RESULTADO
print(f"Os números {numero01} e {numero02} são pares? \n{resto_numero01 + resto_numero02 == 0}")