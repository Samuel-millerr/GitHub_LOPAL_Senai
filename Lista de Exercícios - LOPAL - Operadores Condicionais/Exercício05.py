#EXERCÍCIO 04 - COMPARAÇÃO DE IDADE
idade_01 = int(input("Insira a idade da primeira pessoa: "))
idade_02 = int(input("Insira a idade da segunda pessoa: "))
idade_03 = int(input("Insira a idade da terceira pessoa: "))

if idade_01 < idade_02 and idade_01 < idade_03 or idade_01 == idade_02 < idade_03:
    idade_menor = idade_01
elif idade_02 < idade_01 and idade_02 < idade_03 or idade_02 == idade_03 < idade_01:
    idade_menor = idade_02
elif idade_03 < idade_01 and idade_03 < idade_02 or idade_03 == idade_01 < idade_02:
    idade_menor = idade_03
else:
    idade_menor = ""

if idade_01 > idade_02 and idade_01 > idade_03 or idade_01 == idade_02 > idade_03:
    idade_maior = idade_01
elif idade_02 > idade_01 and idade_02 > idade_03  or idade_02 == idade_03 > idade_01:
    idade_maior = idade_02
elif idade_03 > idade_01 and idade_03 > idade_02 or idade_03 == idade_01 > idade_02:
    idade_maior = idade_03
else:
    idade_maior = ""
    print("Todas as idades são iguais!")

if idade_maior != "":
    print("Segundo o algoritimo, dentre as idades: ")
    print(f"A idade {idade_menor} é a menor.")
    print(f"A idade {idade_maior} é a maior.")
