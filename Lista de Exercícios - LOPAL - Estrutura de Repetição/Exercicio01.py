print("=============================")
print("EXERCÍCIO 01 - MÚLTIPLOS DE 3")
print("=============================\n")

print("Digite 10 números para verificarmos quantos deles são múltiplos de 3.")
numeros_multiplos = 0

# LAÇO PARA VERIFICAR SE É MÚLTIPLO DE 3
for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero % 3 == 0:
        numeros_multiplos += 1
    else:
        numeros_multiplos += 0

print(f"\n{numeros_multiplos} números são múltiplos de 3!\n")
