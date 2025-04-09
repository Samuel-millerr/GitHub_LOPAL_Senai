print("===========================")
print("EXERCÍCIO 06 - PAR OU IMPAR")
print("===========================\n")

print("Digite 10 números interos!")

numeros_pares = []
numeros_impares = []

for i in range(10):
    numero = int(input(f"Insira o {i + 1}° número: "))

    if numero % 2 == 0:
        numeros_pares.append(numero)

    else:
        numeros_impares.append(numero)

print("Os números pares são: ", end='')
for numero in numeros_pares:
    print(f"{numero} ", end='')

print("\nOs números impares são: ", end='')
for numero in numeros_impares:
    print(f"{numero} ", end='')

