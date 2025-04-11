import random
print("===========================")
print("EXERCÍCIO 08 - CARA E COROA")
print("===========================\n")

condicao = 0
while condicao < 3:
    escolha_usuario = input("Cara ou coroa? (Digite qual será sua escolha)\n").strip()
    escolha_maquina  = random.choice(["cara","coroa"])

    if escolha_usuario.lower() == "cara" and escolha_maquina == "cara" or escolha_usuario.lower() == "coroa" and escolha_maquina == "coroa":
        print(f"Caiu {escolha_maquina}")
        print("Você acertou!\n")
    else:
        print(f"Caiu {escolha_maquina}")
        print("Você errou!\n")

    if escolha_maquina == "cara":
        condicao += 1
    else:
        condicao = 0

print("Caiu 3 vezes cara. O jogo acabou!")
