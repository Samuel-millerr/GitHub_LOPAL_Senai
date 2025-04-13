import random
import re

print("==========================")
print("DESAFIO 02 - JOGO DA FORCA")
print("==========================\n")

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
palavra_escolhida_oculta = re.sub(r"[a-zçãáàâãéèêíìîóòôõúùû]", "_", palavra_escolhida) #Ocultação da palavra para demostrar ao usuário
letras_incorretas = []

chances = 6

# Laço While para o jogo rodar enquanto houver chances
while chances > 0:

    # Exibição da palavra escolhida (oculta) e das tentativas restantes
    print(f"A palavra é {palavra_escolhida_oculta}")
    print(f"Você tem {chances} tentativas, no caso de erro as chances diminuirão.")

    # Pedir ao usuário se deseja já chutar alguma palavra ou escolhar alguma letra
    escolha_usuario = int(input("Você já gostaria de tentar adivinhar a palavra? \n( 1 ) Sim\n( 0 ) Não\n"))

    # Estrutura condicional caso o usuário deseje chutar alguma letra
    if escolha_usuario == 1:
        escolha_usuario = input("\nDigite sua palavra para tentar advinhar: ").strip()
        if escolha_usuario.lower() == palavra_escolhida:
            print(f"Parabéns você acertou a palavra! {palavra_escolhida}")
            chances = 0
        else:
            print("Que pena você errou a palavra! Menos uma chance.")
            chances -= 1

    else: # Caso o usuário não deseje adivinhar a palavra ele terá que adivinhar a letra
        escolha_usuario = input("\nDigite uma letra para tentar adivinhar a palavra: ").strip()
        posicao_letra = 0

        # Laço for para percorrer e verificar se a letra que o usuário digitou corresponde dentro do texto e sua posição
        for letra in palavra_escolhida:
            if escolha_usuario.lower() == letra:

                # No caso da letra ser presente, o programa irá substituir todas as ocorrências da palavra
                palavra_escolhida_oculta = palavra_escolhida_oculta[:posicao_letra] + escolha_usuario + palavra_escolhida_oculta[posicao_letra+1:]
                re.sub(letra, "_ ", palavra_escolhida)
                existe_no_texto = True

            else:

                letras_incorretas.append(escolha_usuario.lower())
                existe_no_texto = False
            posicao_letra += 1
        # É necessário uma estrutura de condicional if para printar se a letra esta correta ou não( e se não diminuir uma chace)
        if palavra_escolhida_oculta == palavra_escolhida:
            print(f"Parabéns você acertou a palavra! {palavra_escolhida}")
            chances = 0
