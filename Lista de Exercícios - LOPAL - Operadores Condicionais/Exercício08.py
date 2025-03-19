#EXERCÍCIO 08 - VERIFICAÇÃO DE FORMA
lado_01 = int(input("Insira o primeiro lado: "))
lado_02 = int(input("Insira o segundo lado: "))
lado_03 = int(input("Insira o terceiro lado: "))
lado_04 = int(input("Insira o querto lado: "))

if lado_01 == lado_02 == lado_03 == lado_04:
    print("A forma é um quadrado!")
elif lado_01 == lado_02 and lado_03 == lado_04 or lado_01 == lado_03 and lado_02 == lado_04 or lado_02 == lado_03 and lado_01 == lado_04:
    print("A forma é um retangulo!")
else:
    print("A forma é inválida!")