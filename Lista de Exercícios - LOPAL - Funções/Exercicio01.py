# Exercício 01

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

print(f"{"="*5} Exercício 01 - Calculadora de IMC {"="*5}")
print("Seja bem vindo(a) a calculadora de IMC, por gentileza insira seu peso(KG) e altura(M) abaixo para realizarmos o calculo: ")
peso = float(input("Peso (xx.x): "))
altura = float(input("Altura (x.xx): "))

imc = calculadoraDeImc(peso,altura)
classificacao_imc = classificar_imc(imc)
print("\nSegue abaixo o calculo do IMC e sua classificação: ")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")