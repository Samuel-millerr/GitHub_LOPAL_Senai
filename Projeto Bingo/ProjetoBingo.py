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

numerosBingo = numeros_b+numeros_i+numeros_n+numeros_g+numeros_o

# FUNÇÃO DE CRIAÇÃO DE CARTELA
def sorteador_cartela():
    numeros_cartela_b = random.sample(numeros_b, k=5)
    numeros_cartela_i = random.sample(numeros_i, k=5)
    numeros_cartela_n = random.sample(numeros_n, k=5)
    numeros_cartela_g = random.sample(numeros_g, k=5)
    numeros_cartela_o = random.sample(numeros_o, k=5)

# FUNÇÃO SORTEAR OS NUMEROS
def mostrarInterfaceBingo():
    listaNumerosEscolhidos = []

    def sortearNumeros():
        numeroSorteado = random.choice(numerosBingo)
        labelNumero["text"] = numeroSorteado

        listaNumerosEscolhidos.append(numeroSorteado)
        labelNumerosSorteados["text"] = listaNumerosEscolhidos

        if len(listaNumerosEscolhidos) % 15 == 0:
            listaNumerosEscolhidos.append(("\n"))

        return

    windowBingo = Tk()
    windowBingo.wm_title("Bingo")

    s = ttk.Style(windowBingo)
    s.configure("Frame1.TFrame", background="green")

    labelNumero = ttk.Label(windowBingo, text = " ")
    labelNumero.place(x=399, y=150)

    buttonSortear = ttk.Button(windowBingo, text="Sortear", command=sortearNumeros)
    buttonSortear.place(x=375, y=175)

    frmNumerosSorteados = ttk.Frame(windowBingo, width = 400, height = 200,  padding = 15, style="Frame1.TFrame")
    frmNumerosSorteados.place(x=200, y=220)

    labelNumerosSorteados = ttk.Label(frmNumerosSorteados, text = " ")
    labelNumerosSorteados.place(x=5, y=5)

    windowBingo.geometry("800x500")
    windowBingo.mainloop()


windowInit = Tk()
windowInit.wm_title("Bingo")
frm = ttk.Frame(windowInit, padding=10)
frm.grid(column = 0)
l1 = ttk.Label(frm, text = "Bem vindo ao bingo!!",).grid(row = 1, column = 0, pady = 5)
buttonIniciar = ttk.Button(frm, text = "JOGAR", command=mostrarInterfaceBingo).grid(row = 2, column = 0, pady = 3)
buttonTabela = ttk.Button(frm, text = "CRIAR TABELA", command= sorteador_cartela()).grid(row = 3, column = 0, pady = 3)
buttonExit = ttk.Button(frm, text = "SAIR", command = windowInit.destroy,).grid(row = 4, column = 0, pady = 3)

windowInit.geometry("140x150")
windowInit.mainloop()



