# #Exercício 01
#
# for numero in range (10):
#     if numero % 2 == 0:
#         print(numero)

# #Exercício 02
# cores = ["vermelho", "azul", "verde", "amarelo"] #LISTA
#
# for cor in cores:
#     print(cor)

# #Exercício 03
# soma = 0
#
# for numero in range(101):
#     soma = numero+soma
#
# print(soma)

# #Exercício 04
# numero = int(input("Insira a o número: "))
#
# for multiplicador in range(1,11):
#     print(f"{numero} x {multiplicador} = {numero*multiplicador}")

# #Exercício 05
tamanho_lista = int(input("Insira o tamanho da lista: "))
soma = 0

for i in range(tamanho_lista):
    numero =int(input(f"Digite o {i+1}° numero: "))
    soma += numero


print(soma/tamanho_lista)

numeros = []
for i in range(tamanho_lista):
    numero = int(input(f"Insira o {i+1}° número: "))
    numeros.insert(i, numero)

print(numeros)
print(f"Média: {sum(numeros)/tamanho_lista}")