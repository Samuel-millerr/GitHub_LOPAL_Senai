print("=============================")
print("EXERCÍCIO 01 - MÚLTIPLOS DE 3")
print("=============================\n")

print("Digite 10 números para verificarmos quantos deles são múltiplos de 3.")
numeros_multiplos = 0

# LAÇO PARA VERIFICAR SE É MÚLTIPLO DE 3
for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero % 3 == 0:
        numeros_multiplos += 1
    else:
        numeros_multiplos += 0

print(f"\n{numeros_multiplos} números são múltiplos de 3!\n")

print("====================")
print("EXERCÍCIO 02 - SENHA")
print("====================\n")

senha = input("Defina a senha a ser utilizada: ").strip()

# LAÇO DE VERIFICAÇÃO DE SENHA
i = 0
while True:
    i +=1
    senha_digitada = input(f"\nInsira sua {i}° tentativa: ").strip()
    if senha_digitada == senha:
        print("SENHA CORRETA!")
        break
    print("SENHA INCORRETA!")

print("===================")
print("EXERCÍCIO 03 - MENU")
print("===================\n")

print("AVISO!!! Digite sua opção de escolha somente através do número correspondente a ela.")
escolha = int(input("Gostaria de entrar no menu?\n( 1 ) Sim\n( 0 ) Não\n"))

# LOOP DE SELEÇÃO DO MENU
while escolha == 1:
    escolha = int(input("\nSelecione alguma das opções:\n( 1 ) Continuar no menu\n( 0 ) Sair do menu\n"))
    if escolha == 0:
        break
    elif escolha != 1:
        print("\nEscolha uma opção correta!")
        escolha = 1
    else:
        escolha = 1
print("Obrigado por usar nosso menu!")

print("==========================================")
print("EXERCÍCIO 04 - VERIFICAÇÃO DE NÚMERO PRIMO")
print("==========================================\n")

print("Digite dois números inteiros.")
numero_01 = int(input("Primeiro número: "))
numero_02 = int(input("Segundo número: "))
primo = True

if numero_01 <= 0 or numero_02 <= 0:
    print("Digite um número correto, não exitem números primos negativos.")
else:
    if numero_01 > numero_02:
        numero_01, numero_02 = numero_02, numero_01
    else:
        # VERIFICAÇÃO DE NÚMERO PRIMOS ENTRE OS NÚMEROS ESCOLHIDOS
        for n in range(numero_01+1, numero_02):
            i = 2
            while i < n:
                if n % i == 0:
                    primo = False
                    break

                else:
                    primo = True
                    i += 1

            if primo:
                print(n)

print("===========================")
print("EXERCÍCIO 05 - 3 TENTATIVAS")
print("===========================\n")

senha = "python123"
tentativas = 3
while tentativas >= 0:
    senha_digitada = input("Digite a senha: ").strip()

    if senha == senha_digitada:
        print("SENHA CORRETA! Acesso liberado.")
        break
    elif tentativas == 1:
        print("ACESSO BLOQUEADO! Todas as tentativas foram utilizadas.")
        break
    else:
        tentativas -= 1
        print(f"ACESSO NEGADO! {tentativas} tentativas restantes.")

print("===========================")
print("EXERCÍCIO 06 - PAR OU IMPAR")
print("===========================\n")

print("Digite 10 números interos!")

numeros_pares = []
numeros_impares = []

for i in range(10):
    numero = int(input(f"Insira o {i + 1}° número: "))

    if numero % 2 == 0:
        numeros_pares.append(numero)

    else:
        numeros_impares.append(numero)

print("\nOs números pares são: ", end='')
for numero in numeros_pares:
    print(f"{numero} ", end='')

print("\nOs números impares são: ", end='')
for numero in numeros_impares:
    print(f"{numero} ", end='')

print("=================================")
print("EXERCÍCIO 07 - CONTADOR DE VOGAIS")
print("=================================\n")

frase = input("Digite um frase: ")
quant_letra_a = 0
quant_letra_e = 0
quant_letra_i = 0
quant_letra_o = 0
quant_letra_u = 0

for letra in frase.lower():
    if letra == 'a':
        quant_letra_a += 1
    elif letra == 'e':
        quant_letra_e += 1
    elif letra == 'i':
        quant_letra_i += 1
    elif letra == 'o':
        quant_letra_o += 1
    elif letra == 'u':
        quant_letra_u += 1


print(f"\nA frase '{frase}' possui:")
print (f" {quant_letra_a} letra(s) A\n {quant_letra_e} letra(s) E\n {quant_letra_i} letra(s) I\n {quant_letra_o} letra(s) U\n {quant_letra_u} letra(s) U")

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

print("===================================")
print("EXERCÍCIO 09 - VERIFICAÇÃO DE MÉDIA")
print("===================================\n")

quant_numeros = int(input("Digite a quantidade de número que você deseja verificar: "))
numeros = []
menores_media = 0

for i in range(quant_numeros):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

media = sum(numeros)/quant_numeros

for numero in numeros:
    if numero < media:
        menores_media += 1
    else:
        menores_media += 0

print(f"\nDa seguinte lista de números \n{numeros}")
print(f"\n{menores_media} números são menores que a média. Média: {media:.2f}")

print("===================================")
print("EXERCÍCIO 10 - SEQUÊNCIA DE NÚMEROS")
print("===================================\n")

quant_numeros = int(input("Digite a quantidade de números que deve ter: "))
numeros = [0]

# Laço para pedir ao usuário a quantidade de números desejados
for i in range(quant_numeros):
    numero = int(input(f"Digite o {i + 1}° da sequência: "))
    numeros.append(numero)

# Primeiro laço For para verificar qual o maior número da lista
maior_numero = numeros[0]
for numero in numeros:
     if maior_numero < numero:
         maior_numero = numero
     else:
         maior_numero = maior_numero
numeros.remove(maior_numero) # Remove o maior número da lista

# Segundo laço For para verificar qual o novo maior número da lista (segundo maior número)
maior_numero = numeros[0]
for numero in numeros:
     if maior_numero < numero:
         maior_numero = numero
     else:
         maior_numero = maior_numero

print("\nO segundo maior número da lista é: ",maior_numero)

from time import sleep

print("===============================================")
print("DESAFIO 01 - SIMULAÇÃO DE POPULAÇÕES DE COELHOS")
print("===============================================\n")
sleep(1.3)

print("Você agora irá decidir as principais informações para a simulação!")
taxa_natalidade = float(input("Digite em % qual será a taxa de reprodução dos coelhos (quantos nascerão por geração): "))
taxa_mortalidade = float(input("Digite em % qual será a taxa de mortalidade dos coelhos (quantos irão falecer por geração): "))
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

import random
import re

print("==========================")
print("DESAFIO 02 - JOGO DA FORCA")
print("==========================")

print("--- REGRAS ---")
print(" - A letra deve ser digitada seguindo a sua acentuação (ex: laboratório)\n"
      "    Caso deseje digitar a primeira letra 'o' é necessário colocar a acentuação.")
print(" - Você possui somente 6 chances! A cada erro uma chance será reduzida.")

lista_palavras =  ( # Declaração de todas as palavras possíveis para a forcar
    "casa",
    "bola",
    "pato",
    "gato",
    "mesa",
    "janela",
    "banana",
    "computador",
    "girafa",
    "abacate",
    "laboratório",
    "xilofone",
    "psicólogo",
    "biblioteca",
    "zoológico",
    "helicóptero",
    "arqueologia",
    "microscópio",
    "astronauta",
    "python"
)
palavra_escolhida = random.choice(lista_palavras) # Escolha da palavra para a forca
palavra_escolhida_oculta = "_" * len(palavra_escolhida) #Ocultação da palavra para demostrar ao usuário
letras_corretas = []
letras_incorretas = []

chances = 6
# Laço While para o jogo rodar enquanto houver chances
while chances > 0:
    print(f"\nVocê já escolheu as seguintes letras: {sorted(letras_corretas+letras_incorretas)}") # Mostrar todas as letras que o usuário já escolheu

    # Exibição da palavra escolhida (oculta) e das tentativas restantes
    print(f"""
      _______
     |/      |
     |      ( )
     |      /|\\
     |      / \\
     |       
    _|_     {palavra_escolhida_oculta}
    """)
    print(f"Você tem {chances} tentativas de erro!")

    # Pedir ao usuário se deseja já chutar alguma palavra ou escolhar alguma letra
    escolha_usuario =input("Você já gostaria de tentar adivinhar a palavra? \n( 1 ) Sim\n( 0 ) Não\n").strip()

    # Estrutura condicional caso o usuário deseje chutar alguma letra
    if escolha_usuario.lower() == "1" or escolha_usuario == "sim":
        escolha_usuario = input("\nDigite sua palavra para tentar advinhar: ").strip()
        if escolha_usuario.lower() == palavra_escolhida:
            print(f"Parabéns você acertou a palavra!")
            chances = 0
        else:
            print("Que pena você errou a palavra! Menos uma chance.")
            chances -= 1

    else: # Caso o usuário não deseje adivinhar a palavra ele terá que adivinhar a letra

        # Laço while para verificar se o usuário já digitou a letra
        i = 1
        while i == 1:
            escolha_usuario = input("\nDigite uma letra para tentar adivinhar a palavra: ").strip()
            if escolha_usuario in (letras_corretas+letras_incorretas):
                print("Você já escolheu essa letra, tente novamente!")
            else:
                posicao_letra = 0
                i = 0

        # Laço for para percorrer e verificar se a letra que o usuário digitou corresponde dentro do texto e sua posição
        for letra in palavra_escolhida:
            if escolha_usuario.lower() == letra:
                # No caso da letra ser presente, o programa irá substituir todas as ocorrências da palavra
                palavra_escolhida_oculta = palavra_escolhida_oculta[:posicao_letra] + escolha_usuario + palavra_escolhida_oculta[posicao_letra+1:]

            else:
                palavra_escolhida_oculta = palavra_escolhida_oculta
            posicao_letra += 1

        # Adição das letras escolhidas do usuário em uma lista para exibição futura
        if escolha_usuario in palavra_escolhida:
            print("Parabéns! você acertou uma letra.")
            letras_corretas.append(escolha_usuario)
        else:
            print(f"Que pena, a letra '{escolha_usuario}', não está na palavra. Você perdeu uma chance!")
            letras_incorretas.append(escolha_usuario)
            chances -= 1

        # Verificão caso o usuário acerte a palavra por meio das letras
        if palavra_escolhida_oculta == palavra_escolhida:
            print(f"Parabéns você acertou a palavra!")
            chances = 0
        elif chances == 0:
            print("Que pena! Todas as suas tentativas acabaram.")
            chances = 0

print(f"A palavra é '{palavra_escolhida}'")

