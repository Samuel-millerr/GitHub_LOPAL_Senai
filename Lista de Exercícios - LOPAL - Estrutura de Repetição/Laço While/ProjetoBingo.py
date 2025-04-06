#Bingo
import random

print("Gostaria de jogar bingo?")
print("(1) Sim\n(0) Não")
condicao = int(input().strip())


if condicao == 1:
    x = 1

    # Definição dos numeros da cartela
    numeros_b = []
    for i in range(15):
        numeros_b.append("B" + str(i + 1))

    numeros_i = []
    for i in range(15, 30):
        numeros_i.append("I" + str(i + 1))

    numeros_n = []
    for i in range(30, 45):
        numeros_n.append("N" + str(i + 1))

    numeros_g = []
    for i in range(45, 60):
        numeros_g.append("G" + str(i + 1))

    numeros_o = []
    for i in range(60, 75):
        numeros_o.append("O" + str(i + 1))

    numeros_bingo = (numeros_b + numeros_i + numeros_n + numeros_g + numeros_o)
    # Sortear os números e mostrar para o usuário
    while x == 1:
        print(random.choice(numeros_bingo))
        continuar = int(input("(1) Sortear mais um número \n(0) Sair\n").strip())
        if continuar == 1:
            x = 1
        else:
            x = 0
            print("JOGO ENCERRADO!")
else:
    print("JOGO ENCERRADO!")

