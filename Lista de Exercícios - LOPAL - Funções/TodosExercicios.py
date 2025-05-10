from time import sleep
def calculadoraDeImc(peso, altura):
    imc = peso/(altura**2)
    return imc

def classificar_imc(imc):
    if imc > 40: classificacao = "Obesidade Grau III"
    elif imc >= 35: classificacao = "Obesidade Grau II"
    elif imc >= 30: classificacao = "Obesidade Grau I"
    elif imc >= 25: classificacao = "Sobrepeso"
    elif imc >= 18.6: classificacao = "Normal"
    elif imc > 0: classificacao = "Abaixo do Normal"
    else: classificacao = "Valor Inválido"
    return classificacao

def maior_n(lista):
    maior_numero = 0
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
        else:
            maior_numero = maior_numero
    return maior_numero

def converter_celsius_para_fahrenheit(temperatura):
    fahrenheit_funcao = temperatura * 1.8 + 32
    return fahrenheit_funcao


def calcular_troco(valor_compra, valor_pago):
    troco = valor_pago - valor_compra
    if troco <= 0:
        print(f"\n{0}! Pagamento insuficiente para realizar a compra.")
    else:
        print(f"\nTroco: R${troco}. Pagamento realizado com sucesso!")
    print("Obrigado por comparecer em nossa loja. Volte sempre!")

def eh_primo(num):
    primo = False
    for i in range(2, num):
        if num == 1:
            primo = False
        elif num % i == 0:
            primo = False
            break
        else:
            primo = True
    return primo

def contar_vogais(palavra):
    qtd_a, qtd_e, qtd_i, qtd_o, qtd_u = 0, 0, 0, 0, 0

    for letra in palavra.lower():
        if letra == "a":
            qtd_a += 1
        elif letra == "e":
            qtd_e += 1
        elif letra == "i":
            qtd_i += 1
        elif letra == "o":
            qtd_o += 1
        elif letra == "u":
            qtd_u += 1
    soma_vogais = qtd_a+qtd_e+qtd_i+qtd_o+qtd_u

    exibir_contagem = {
        "Quantidade de Vogais: ": soma_vogais,
        "Letra A: ": qtd_a,
        "Letra E: ": qtd_e,
        "Letra I: ": qtd_i,
        "Letra O: ": qtd_o,
        "Letra U: ": qtd_u
    }
    return exibir_contagem

def contagem_regressiva(num):
    if num == 0:
        print(0)
        print("A contagem acabou!")
    else:
        print(num)
        sleep(0.6)
        return contagem_regressiva(num - 1)

# Exercício 01
print(f"\n{"="*5} Exercício 01 - Calculadora de IMC {"="*5}")
print("Seja bem vindo(a) a calculadora de IMC, por gentileza insira seu peso(KG) e altura(M) abaixo para realizarmos o calculo: ")
peso = float(input("Peso (xx.x): "))
altura = float(input("Altura (x.xx): "))

imc = calculadoraDeImc(peso,altura)
classificacao_imc = classificar_imc(imc)
print("\nSegue abaixo o calculo do IMC e sua classificação: ")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")

# Exercício 02
print(f"\n{"="*5} Exercício 02 - Verificação de Número Maior {"="*5}")
listaNumeros = []
print("O programa irá realizar a verificação de qual é o maior número em uma determinada lista.")
quantNumeros = int(input("Insira a quantidade de números que você deseja inserir: "))
for i in range(quantNumeros):
    numero = float(input(f"Digite o {i + 1}° número: "))
    listaNumeros.append(numero)

print(f"O maior número entre a seguinte lista {listaNumeros} é {maior_n(listaNumeros):.1f}")

# Exercício 03
print(f"\n{"="*5} Exercício 03 - Conversor de Temperatura {"="*5}")
print("Bem vindo(a) ao conversor de temperatura de Celsius ----> Fahrenheit!")
print("Insira a temperatura em Celsius para realizar a conversão")
celsius = float(input(" > "))

fahrenheit = converter_celsius_para_fahrenheit(celsius)
print(" °Celsius ----> °Fahrenheit")
print(f" °{celsius:.1f}     ----> °{fahrenheit:.1f}")

# Exercício 04
print(f"\n{"="*5} Exercício 04 - Lojinha {"="*5}")
print("Bem vindo a lojinha, insira as informações abaixo para acabar o atendimento: ")
valor_compra = float(input("Insira qual foi o valor total de sua compra: "))
forma_pagamento = input("Escolha sua forma de pagamento: \n[1] Pix \n[2] Credito\n[3] Débito\n > ")
valor_pago = float(input("Insira qual valor foi usado para pagar a compra: "))

calcular_troco(valor_compra, valor_pago)

# Exercício 05
print(f"\n{"="*5} Exercício 05 - Verificador de Número Primo {"="*5}")
print("Olá, insira algum número para o programa verificar se ele é primo ou não.")
numero = int(input(" > "))

ehPrimo = eh_primo(numero)
print(f"O número {numero} é primo? {ehPrimo}")

# Exercício 06
print(f"\n{"="*5} Exercício 06 - Contar Vogais {"="*5}")
print("Insira a suva palavra para realizarmos a contagem de vogais: ")
texto = input(" > ")

print("\nSegue abaixo a contagem sobre a palavra/frase digitada: ")
contagem = contar_vogais(texto)
for chave, valor in contagem.items():
    print(chave, valor)

# Exercício 07
print(f"\n{"="*5} Exercício 07 - Contagem Regressiva {"="*5}")
numero = int(input("Insira o número para ser realizado a contagem: "))
contagem_regressiva(numero)
