#DESAFIO 01 - ACERTE O NÚMERO
import random
print("O computador escolheu um número!! Ele está entre 1 e 10, tente advinhar qual é. Você tem duas tentativas. Boa sorte!!")
numero_usuario = int(input("Digite o número: "))
numero_computador = random.randint(1, 10)
tentativas = 1


if numero_usuario > 10 or numero_usuario < 0:
   print("Esse número é inválido, escolha um número de 1 a 10.")
elif numero_usuario == numero_computador:
   print(f"\nParabéns você acertou!! O computador escolheu o número {numero_computador}.")
else:
   print(f"\nVocê errouuu!! {tentativas} tentativa restante.")
   if numero_usuario < numero_computador:
       print("DICA: O número do computador é maior que o seu palpite.")
   else:
       print("DICA: O número do computador é menor que o seu palpite.")
   numero_usuario = int(input("Digite o número: "))
   if numero_usuario == numero_computador:
       print(f"\nParabéns você acertou!! O computador escolheu o número {numero_computador}.")
   else:
       print(f"\nQue pena, você não consegui acertar!! O número escolhido pelo computador foi {numero_computador}. Boa sorte na próxima!")
