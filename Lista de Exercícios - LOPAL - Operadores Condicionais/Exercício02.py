#EXERCÍCIO 02 - CALCULADORA DE IMC
peso = float(input("Insira o peso da pessoa, em KG: "))
altura = float(input("Insira a altura da pessoa, em M: "))

imc = peso/altura**2

print(f"O IMC dessa pessoa é de {imc:.2f}")

if imc < 18.5:
    print("Essa pessoa esta na faixa de Abaixo do Peso")
elif imc < 25:
    print("Essa pessoa esta na faixa de peso normal.")
elif imc < 30:
    print("Essa pessoa esta na faixa de Sobrepeso.")
elif imc < 35:
    print("Essa pessoa esta na faixa de Obesidade.")
elif imc < 40:
    print("Essa pessoa esta na faixa de Obesidade Mórbida I.")
else:
    print("Essa pessoa esta na faixa de Obesidade Mórbida II.")