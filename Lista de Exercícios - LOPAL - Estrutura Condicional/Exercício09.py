#EXERCÍCIO 09 - CALCULADORA SIMPLES
print("Insira ambos os números com ao menos uma casa decimal - Exemplo: 2.45")
numero_01 = float(input("Insira o primeiro número para realizar a operação: "))
numero_02 = float(input("Insira o segundo número para realizar a operação: "))
operacao = input("Escolha a operação desejada: \n(+)Soma \n(-)Subtração \n(*)Multiplicação \n(/)Divisão \n").strip()

if numero_01 % 1 == 0 or numero_02 % 1 == 0:
    calculo = "sem_decimal"
    tipo_de_conta = "none"
elif operacao == "+":
    calculo = numero_01 + numero_02
    tipo_de_conta = "soma"
elif operacao == "-":
    calculo = numero_01 - numero_02
    tipo_de_conta = "subtração"
elif operacao == "*":
    calculo = numero_01 * numero_02
    tipo_de_conta = "multiplicação"
elif operacao == "/":
    calculo = numero_01 / numero_02
    tipo_de_conta = "divisão"
else:
    calculo = "none"
    tipo_de_conta = "none"


if calculo == "none":
    print("O digito da conta está inválido!")
    print("Por gentileza tente novamente!")
elif calculo == "sem_decimal":
    print("Algum dos números não possui casas decimais!")
    print("Por gentileza tente novamente!")
else:
    print(f"A operação escolhida é {tipo_de_conta} e o resultado é {calculo:.1f}")

