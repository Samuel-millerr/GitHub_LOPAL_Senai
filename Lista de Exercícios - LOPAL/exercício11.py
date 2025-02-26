#EXERCÍCIO 11 - CALCULADORA DE IMC
#PEDE OS VALORES AO USUÁRIO
peso = float(input("Insira seu peso em KG: "))
altura = float(input("Insira sua altura em METROS: "))

#CALCULO DO IMC
imc = peso/(altura** 2)

#IMPRESSÃO DO RESULTADO
print(f"O seu IMC é de {imc:.2f}")

