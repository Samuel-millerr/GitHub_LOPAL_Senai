# Exercício 02

def maior_n(lista):
    maior_numero = 0
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
        else:
            maior_numero = maior_numero
    return maior_numero

print(f"{"="*5} Exercício 02 - Verificação de Número Maior {"="*5}")
listaNumeros = []
print("O programa irá realizar a verificação de qual é o maior número em uma determinada lista.")
quantNumeros = int(input("Insira a quantidade de números que você deseja inserir: "))
for i in range(quantNumeros):
    numero = float(input(f"Digite o {i + 1}° número: "))
    listaNumeros.append(numero)

print(f"O maior número entre a seguinte lista {listaNumeros} é {maior_n(listaNumeros):.1f}")