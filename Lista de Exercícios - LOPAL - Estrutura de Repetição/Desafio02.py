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
palavra_escolhida_oculta = re.sub(r"[a-zçãáàâãéèêíìîóòôõúùû]", "_", palavra_escolhida) #Ocultação da palavra para demostrar ao usuário
letras_corretas = []
letras_incorretas = []

chances = 6
# Laço While para o jogo rodar enquanto houver chances
while chances > 0:
    print(f"\nVocê já escolheu as seguinte letras {sorted(letras_corretas+letras_incorretas)}")

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
    escolha_usuario = int(input("Você já gostaria de tentar adivinhar a palavra? \n( 1 ) Sim\n( 0 ) Não\n"))

    # Estrutura condicional caso o usuário deseje chutar alguma letra
    if escolha_usuario == 1:
        escolha_usuario = input("\nDigite sua palavra para tentar advinhar: ").strip()
        if escolha_usuario.lower() == palavra_escolhida:
            print(f"Parabéns você acertou a palavra!")
            chances = 0
        else:
            print("Que pena você errou a palavra! Menos uma chance.")
            chances -= 1

    else: # Caso o usuário não deseje adivinhar a palavra ele terá que adivinhar a letra

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

        if escolha_usuario in palavra_escolhida:
            print("Parabéns! você acertou uma letra.")
            letras_corretas.append(escolha_usuario)
        else:
            print(f"Que pena, a letra '{escolha_usuario}', não está na palavra.")
            letras_incorretas.append(escolha_usuario)
            chances -= 1

        if palavra_escolhida_oculta == palavra_escolhida:
            print(f"Parabéns você acertou a palavra!")
            chances = 0

print(f"A palavra é '{palavra_escolhida}'")