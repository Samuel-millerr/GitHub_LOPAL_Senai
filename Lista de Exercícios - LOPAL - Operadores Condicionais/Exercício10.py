#EXERCÍCIO 10 - CALCULADORA DE MÉDIA COM DESCARTE
nota_01 = float(input("Digite a primeira nota do aluno: "))
nota_02 = float(input("Digite a segunda nota do aluno: "))
nota_03 = float(input("Digite a terceira nota do aluno: "))

if nota_01 < nota_02 and nota_01 < nota_03:
    media = (nota_02 + nota_03)/2
elif nota_02 < nota_01 and nota_02 < nota_03:
    media = (nota_01 + nota_03)/2
elif nota_03 < nota_01 and nota_03 < nota_02:
    media = (nota_01 + nota_02)/2
elif nota_01 == nota_02 == nota_03:
    media = ""
    print("Todas as notas são iguais! Não é possível realizar o descarte da menor nota.")
else:
    media = ""
    print("Não é possível realizar o descarte das notas pois duas notas são iguais e menores que a nota restante!")

if media != "":
    print(f"A média das notas é {media}")
