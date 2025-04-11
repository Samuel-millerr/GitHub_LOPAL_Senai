print("===================================")
print("EXERCÍCIO 09 - VERIFICAÇÃO DE MÉDIA")
print("===================================\n")

quant_numeros = int(input("Digite a quantidade de número que você deseja verificar: "))
numeros = []
menores_media = 0

for i in range(quant_numeros):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

media = sum(numeros)/quant_numeros

for numero in numeros:
    if numero < media:
        menores_media += 1
    else:
        menores_media += 0

print(f"\nDa seguinte lista de números \n{numeros}")
print(f"\n{menores_media} números são menores que a média. Média: {media:.2f}")
