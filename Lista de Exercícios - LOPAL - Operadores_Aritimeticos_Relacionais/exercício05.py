#EXERCÍCIO 05 - VERIFICAÇÃO DE PARES
#PEDE OS NÚMEROS AO USUÁRIO
numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

#CALCULO E IMPRESSÃO DO RESULTADO
print(f"Os números {numero01} e {numero02} são pares? \n{(numero01 % 2) + (numero02 % 2) == 0}")
