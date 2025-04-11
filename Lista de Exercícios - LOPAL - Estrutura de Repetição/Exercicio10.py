print("===================================")
print("EXERCÍCIO 10 - SEQUÊNCIA DE NÚMEROS")
print("===================================\n")

quant_numeros = int(input("Digite a quantidade de números que deve ter: "))
numeros = []

for i in range(quant_numeros):
    numero = int(input(f"Digite o {i + 1}° da sequência: "))
    numeros.append(numero)

maior_numero = numeros[0]
for numero in numeros:
     if maior_numero < numero:
         maior_numero = numero
     else:
         maior_numero = maior_numero

print(maior_numero)