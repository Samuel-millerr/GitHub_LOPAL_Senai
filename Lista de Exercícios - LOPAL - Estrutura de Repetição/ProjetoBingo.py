# BINGO
from tkinter import *
from tkinter import ttk
import random

# DEFINIÇÃO DOS NÚMEROS DA CARTELA
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

# FUNÇÃO DE CRIAÇÃO DE CARTELA
def sorteador_cartela():
    numeros_cartela_b = random.sample(numeros_b, k=5)
    numeros_cartela_i = random.sample(numeros_i, k=5)
    numeros_cartela_n = random.sample(numeros_n, k=5)
    numeros_cartela_g = random.sample(numeros_g, k=5)
    numeros_cartela_o = random.sample(numeros_o, k=5)

    # SORTEAR OS NÚMERO E MOSTRAR PARA O USUÁRIO
#     numeros_escolhidos = []
#     numeros_bingo = (numeros_b + numeros_i + numeros_n + numeros_g + numeros_o)
#     while condicao == 1:
#         numero_escolhido = random.choice(numeros_bingo)
#         numeros_escolhidos.append(numero_escolhido)
#         print(f"O número sorteado foi {numero_escolhido}")
#
#         condicao = int(input("(1) Sortear mais um número \n(2) Ver os números escolhidos \n(0) Sair\n").strip())
#         if condicao == 1:
#             condicao = 1
#         elif condicao == 2:
#             condicao = 1
#             print(f"\nOs números escolhidos até agora foram: {numeros_escolhidos}")
#         else:
#             print("JOGO ENCERRADO!")
# else:
#     print("JOGO ENCERRADO!")

window = Tk()
window.wm_title("Bingo")
frm_1 = ttk.Frame(window, padding=10)
frm_1.grid(column = 5)
l1 = ttk.Label(frm_1, text = "Bem vindo ao bingo!!",).grid(row = 1, column = 0, pady = 5)
button_play = ttk.Button(frm_1, text = "JOGAR").grid(row = 2, column = 0, pady = 3)
button_tabela = ttk.Button(frm_1, text = "CRIAR TABELA", command= sorteador_cartela()).grid(row = 3, column = 0, pady = 3)
button_exit = ttk.Button(frm_1, text = "SAIR", command = window.destroy).grid(row = 4, column = 0, pady = 3)


window.geometry("512x512")
window.mainloop()

