#EXERCÍCIO 04 - COMPARAÇÃO DE IDADE
idade_01 = int(input("Insira a idade da primeira pessoa: "))
idade_02 = int(input("Insira a idade da segunda pessoa: "))
idade_03 = int(input("Insira a idade da terceira pessoa: "))

if idade_01 == idade_02 == idade_03 == idade_01:
    print(f"{idade_01}, {idade_02}, {idade_03}")
    print("As idades são todas iguais ")
elif idade_01 == idade_02 and idade_01 and idade_02 > idade_03:
    print(f"A idade {idade_03} é a menor")
    print(f"A idade {idade_02} é a maior")
elif idade_01 == idade_03 and idade_01 and idade_03 > idade_02: