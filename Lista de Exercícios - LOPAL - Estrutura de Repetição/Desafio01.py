from time import sleep

print("===============================================")
print("DESAFIO 01 - SIMULAÇÃO DE POPULAÇÕES DE COELHOS")
print("===============================================\n")
sleep(1.3)

print("Você agora irá decidir as principais informações para a simulação!")
taxa_natalidade = float(input("Digite em % qual será a taxa de reprodução dos coelhos (quantos nascerão por geração): "))
taxa_mortalidade = float(input("Digite em % qual será a taxa de mortalidade dos coelhos (quantos irão falecer por geração: "))
coelhos_iniciais = int(input("Digite qual será a quantidade de coelhos no inicio da simulação: "))
quantidade_geracoes = int(input("Digite qual será a quantidade de gerações que a simulação deve fazer: "))

geracao = 1
if coelhos_iniciais <= 2: print("Não é possível realizar uma simulação com apenas um coelho!"); geracao = quantidade_geracoes
elif quantidade_geracoes <= 1: print("Para realizar a simulação é necessário ao menos 2 gerações!"); geracao = quantidade_geracoes+1
else:
    coelhos_geracao = coelhos_iniciais
    crescimento_vegetativo = (taxa_natalidade/100) - (taxa_mortalidade/100)
    while geracao <= quantidade_geracoes:
        coelhos_nasceram = coelhos_geracao*(taxa_natalidade/100)
        coelhos_faleceram = coelhos_geracao*(taxa_mortalidade/100)
        coelhos_geracao = coelhos_geracao + (coelhos_geracao*crescimento_vegetativo)
        print(f"\n--- {geracao}º geração ---")
        print(f"{coelhos_nasceram:.0f} coelhos nasceram.")
        print(f"{coelhos_faleceram:.0f} coelhos faleceram.")
        print(f"Quantidade de coelhos: {coelhos_geracao:.0f}.")
        geracao += 1

    print(f"\nApós {geracao-1}º gerações a população de coelhos é de {coelhos_geracao:.0f}")

