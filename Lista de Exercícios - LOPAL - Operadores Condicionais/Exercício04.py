#EXERCÍCIO 04 - VERIFICAÇÃO DE VOTO
idade = int(input("Insira a idade do eleitor: "))

if idade < 16:
    print(f"Voto PROIBIDO!")
elif idade < 18:
    print(f"O eleitor tem {idade} anos, o voto é FACULTATIVO!")
elif idade <= 59:
    print(f"O eleitor tem {idade} anos, o voto é OBRIGATÓRIO!")
else:
    print(f"O eleitor tem {idade} anos, o voto é FACULTATIVO!")