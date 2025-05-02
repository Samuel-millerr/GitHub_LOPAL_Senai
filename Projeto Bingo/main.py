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


listaNumerosEscolhidos = []
def sortearNumeros():
    numeroSorteado = random.choice(numerosBingo)
    listaNumerosEscolhidos.append(numeroSorteado)
    print(numeroSorteado)
    return

sortearNumeros()
