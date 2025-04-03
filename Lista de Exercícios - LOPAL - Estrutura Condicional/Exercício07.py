#EXERCÍCIO 07 - VERIFICAÇÃO DE NOTA
nota = float(input("Insira a nota da prova do usuário: "))

if 0 <= nota < 3:
    print(f"A nota {nota:.1f} é E!")
elif 0 <= nota < 5:
    print(f"A nota {nota:.1f} é D!")
elif 0 <= nota < 7:
    print(f"A nota {nota:.1f} é C!")
elif 0 <= nota < 9:
    print(f"A nota {nota:.1f} é B!")
elif 0 <= nota <= 10:
    print(f"A nota {nota:.1f} é A")
else:
    print(f"A nota {nota:.1f} é inválida!")
