# Exercício 02
print(f"{"="*5} Exercício 02 - Verificação de Número Maior {"="*5}")

def maior_n(lista):
    maiorNumero = 0
    for numero in lista:
        if numero > maiorNumero:
            maiorNumero = numero
        else:
            maiorNumero = maiorNumero
    return maiorNumero

listaNumeros = []
print("O programa irá realizar a verificação de qual é o maior número em uma determinada lista.")
quantNumeros = int(input("Insira a quantidade de números que você deseja inserir: "))
for i in range(quantNumeros):
    numero = float(input(f"Digite o {i + 1}° número: "))
    listaNumeros.append(numero)

print(f"O maior número entre a seguinte lista {listaNumeros} é {maior_n(listaNumeros):.1f}")