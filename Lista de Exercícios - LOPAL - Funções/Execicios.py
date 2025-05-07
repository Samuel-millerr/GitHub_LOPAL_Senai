# Exercício 01
# def dobro(numero):
#     media = numero*2
#     return media
#
# numero = float(input("Insira o número para ser calculado o dobro: "))
# print(f"O dobro do número {numero:.1f} é {dobro(numero):.1f}")

# Exercício 02
# def maior(num01, num02):
#     if num01 > num02:
#         numeroMaior = f"O número {num01} é o maior"
#     elif num02 > num01:
#         numeroMaior = f"O número {num02} é o maior"
#     else:
#         numeroMaior = "Os dois números são iguais"
#     return numeroMaior
#
# num01 = int(input("Insira o primeiro número: "))
# num02 = int(input("Insira o segundo número: "))
#
# print(maior(num01, num02))

# Exercício 03
# def media(lista):
#     media = sum(lista)/len(lista)
#     return media
#
# lista = []
# tamanhoLista = int(input("Defina o tamanho da lista de números: "))
# for i in range(tamanhoLista):
#     numero = int(input(f"Digite o {i+1}° número: "))
#     lista.append(numero)
#
# print(f"Média: {media(lista)}")

#Exercício 04
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    return fatorial

numero = int(input("Insira o número para ser calculado o fatorial: "))
print(f"{numero}! = {calcular_fatorial(numero)}")
