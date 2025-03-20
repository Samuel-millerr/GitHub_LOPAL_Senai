#EXERCÍCIO 07 - VERIFICAÇÃO DE NOTA
nota = float(input("Insira a nota da prova do usuário: "))

if nota < 3:
    print(f"A nota {nota:.1f} é E!")
elif nota < 5:
    print(f"A nota {nota:.1f} é D!")
elif nota < 7:
    print(f"A nota {nota:.1f} é C!")
elif nota < 9:
    print(f"A nota {nota:.1f} é B!")
elif nota <= 10:
    print(f"A nota {nota:.1f} é A")
else:
    print(f"A nota {nota:.1f} é inválida!")