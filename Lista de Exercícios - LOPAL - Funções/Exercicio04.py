# Exercício 04

def calcular_troco(valor_compra, valor_pago):
    troco = valor_pago - valor_compra
    if troco <= 0:
        print(f"\n{0}! Pagamento insuficiente para realizar a compra.")
    else:
        print(f"\nTroco: R${troco}. Pagamento realizado com sucesso!")
    print("Obrigado por comparecer em nossa loja. Volte sempre!")

print(f"{"="*5} Exercício 04 - Lojinha {"="*5}")
print("Bem vindo a lojinha, insira as informações abaixo para acabar o atendimento: ")
valor_compra = float(input("Insira qual foi o valor total de sua compra: "))
forma_pagamento = input("Escolha sua forma de pagamento: \n[1] Pix \n[2] Credito\n[3] Débito\n > ")
valor_pago = float(input("Insira qual valor foi usado para pagar a compra: "))

calcular_troco(valor_compra, valor_pago)