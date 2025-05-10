from time import sleep
# Exercício 07

def contagem_regressiva(num):
    if num == 0:
        print(0)
        print("A contagem acabou!")
    else:
        print(num)
        sleep(0.6)
        return contagem_regressiva(num - 1)

print(f"{"="*5} Exercício 07 - Contagem Regressiva {"="*5}")
numero = int(input("Insira o número para ser realizado a contagem: "))
contagem_regressiva(numero)
