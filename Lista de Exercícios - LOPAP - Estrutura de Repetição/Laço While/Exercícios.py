# Exercício 01
# numero = int(input("Digite um número de 5 a 10: "))
#
# if 5 <= numero <= 10:
#     print(f"O número escolhido foi {numero}, sua contagem regressiva é: ")
#     while numero >= 0:
#         print(numero)
#         numero -= 1
# else:
#     print("O número deve ser de 5 a 10.")
#

#Exercício 02
# contador = 1
# numero_maior = 0
# while contador <= 5:
#     numero = int(input(f"Digite o {contador}° numero: "))
#     if numero > numero_maior:
#         numero_maior = numero
#     contador += 1
#
# print(numero_maior)

#Exercício 03
# resultado = 1
# numero = int(input("Digite um número para ser calculado o fatorial: "))
# numero_mostrar = numero
# while numero >= 1:
#     resultado = resultado*numero
#     print(resultado)
#     numero -= 1
# print(f"O fatorial do número {numero_mostrar} é {resultado}")

#Exercicio 04
# tamanho_lista = int(input("Digite o tamanho da lista desejada: "))
# tamanho_lista_exibir = tamanho_lista
# contador = 1
# soma = 0
# while tamanho_lista >= 1:
#     nota = float(input(f"Digite a {contador}° nota: "))
#     soma = soma + nota
#     tamanho_lista -= 1
#     contador += 1
#
# print(soma/tamanho_lista_exibir)

#Exercicio 05
# escolha = 1
# while escolha != 0:
#     print("Escolha a operação que você deseja realizar: ")
#     print("- Soma (+) ")
#     print("- Subtração (-) ")
#     print("- Multiplicação (*) ")
#     print("- Divisão (/) ")
#     print("- Sair (0) ")
#     escolha = input("")
#     if escolha != "0":
#         numero_01 = int(input("Insira o primeiro número para realizar a conta: "))
#         numero_02 = int(input("Insira o segundo número para realizar a conta: "))
#         if escolha == "+":
#             conta = numero_01 + numero_02
#         elif escolha == "-":
#             conta = numero_01 - numero_02
#         elif escolha == "*":
#             conta = numero_01 * numero_02
#         elif escolha == "/":
#             conta = numero_01/numero_02
#         else:
#             conta = "0"
#
#         if conta == "0":
#             print("Escolha uma opção de conta correta!")
#         else:
#             print(f"O resultado da conta é {conta:.2f}.")
#     else:
#         escolha = 0

#Bingo
import random

print("Gostaria de jogar bingo?")
print("Sim\nNão")
condicao = input("Escolha:").strip()
if condicao == "sim":

    numeros_b = []
    for i in range(15):
        numeros_b.append(i)
    numero_i =
    numeros_n =
    numeros_g =
    numero_o =
    while condicao == "sim":


else:
    print("JOGO ENCERRADO!")