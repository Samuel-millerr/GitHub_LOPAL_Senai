#Bingo
import random

print("Gostaria de jogar bingo?")
print("(1) Sim\n(0) Não")
condicao = int(input().strip())

if condicao == 1:

    #DEFINIÇÃO DOS NÚMEROS DA CARTELA
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

    #FUNÇÃO DE CRIAÇÃO DE CARTELA
    def sorteador_cartela():
        numeros_cartela_b = random.sample(numeros_b, k=5)
        print(numeros_cartela_b)
        numeros_cartela_i = random.sample(numeros_i, k=5)
        print(numeros_cartela_i)
        numeros_cartela_n = random.sample(numeros_n, k=5)
        print(numeros_cartela_b)
        numeros_cartela_g = random.sample(numeros_g, k=5)
        print(numeros_cartela_b)
        numeros_cartela_o = random.sample(numeros_o, k=5)
        print(numeros_cartela_b)
    sorteador_cartela()

    #SORTEAR OS NÚMERO E MOSTRAR PARA O USUÁRIO
    while condicao == 1:
        numeros_bingo = (numeros_b + numeros_i + numeros_n + numeros_g + numeros_o)
        print(random.choice(numeros_bingo))
        condicao = int(input("(1) Sortear mais um número \n(0) Sair\n").strip())
        if condicao == 1:
            condicao = 1
        else:
            print("JOGO ENCERRADO!")
else:
    print("JOGO ENCERRADO!")

