print("===================================")
print("EXERCÍCIO 10 - SEQUÊNCIA DE NÚMEROS")
print("===================================\n")

quant_numeros = int(input("Digite a quantidade de números que deve ter: "))
numeros = [0]

# Laço para pedir ao usuário a quantidade de números desejados
for i in range(quant_numeros):
    numero = int(input(f"Digite o {i + 1}° da sequência: "))
    numeros.append(numero)

# Primeiro laço For para verificar qual o maior número da lista
maior_numero = numeros[0]
for numero in numeros:
     if maior_numero < numero:
         maior_numero = numero
     else:
         maior_numero = maior_numero
numeros.remove(maior_numero) # Remove o maior número da lista

# Segundo laço For para verificar qual o novo maior número da lista (segundo maior número)
maior_numero = numeros[0]
for numero in numeros:
     if maior_numero < numero:
         maior_numero = numero
     else:
         maior_numero = maior_numero

print("\nO segundo maior número da lista é: ",maior_numero)