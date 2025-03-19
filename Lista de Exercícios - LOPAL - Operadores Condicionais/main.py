import random

#EXERCICIO 01
"""idade = int(input("Insira a sua idade: "))

if idade >= 18:
    print("Essa pessoa é maior de idade!")
else:
    print("Essa pessoa é menor de idade!")"""

#EXERCICIO 02
"""nota = float(input("Insira a respectiva nota do aluno: "))

if nota >= 9.0:
    print(f"A nota {nota} é exelente!")
elif nota >= 7.0:
    print(f"A nota {nota} é boa!")
elif nota >= 5.0:
    print(f"A nota {nota} é média!")
else:
    print(f"A nota {nota} é insuficiente!")"""

#EXERCICIO 03
""""numero = int(input("Insira o número para verificação de par ou impar: "))

if numero % 2 != 0:
    print("O número é impar!")
else:
    print("O número é par!")


if numero % 3 == 0:
    print("O número é múltiplo de 3")
else:
    print("O número não é multiplo de 3")

if numero % 5 == 0:
    print("O número é múltiplo de 5")
else:
    print("O número não é multiplo de 5")"""

#EXERCICIO 04
"""numero_01 = float(input("Digite o primeiro número: "))
numero_02 = float(input("Digite o segundo número: "))

if numero_01 == numero_02:
    print(f"Os números {numero_01} e {numero_02} são iguais!")
elif numero_01 > numero_02:
    print(f"O número {numero_01} é maior que o {numero_02}!")
else:
    print(f"O número {numero_02} é maior que o {numero_01}!")"""

#EXERCICIO 05
"""idade = int(input("Insira a a idade correspondente: "))

if idade < 2:
    print("A idade correspondente é de um bebe!")
elif idade < 13:
    print("A idade correspondente é de uma criança!")
elif idade < 18:
    print("A idade correspondente é de um adolescente!")
elif idade < 60:
    print("A idade correspondente é de um adulto!")
else: 
    print("A idade correspondente é de um idoso!")"""

#EXERCICIO 06
"""print("Digite o número de qual conversão você deseja realizar: \n1) Celsius -----> Fahrenheit \n2) Fahrenheit -----> Celsius")
tipo_de_conversao = int(input())
temperatura = float(input("Insira a temperatura a ser convertida: "))

if tipo_de_conversao == 1:
    conversao = (temperatura * 9/5) + 32
    print(f"{temperatura:.2f}C° convertido para celsius é {conversao:.2f}F°")
elif tipo_de_conversao == 2:
    conversao = (temperatura - 32) * 5/9
    print(f"{temperatura:.2f}F° convertido para celsius é {conversao:.2f}C°")
else:
    print("O número é inválido!")"""

#EXERCICIO 07
"""lado_01 = int(input("Insira o primeiro lado do triangulo: "))
lado_02 = int(input("Insira o segundo lado do triangulo: "))
lado_03 = int(input("Insira o terceiro lado do triangulo: "))

if lado_01 < lado_02+lado_03 and lado_02 < lado_01+lado_03 and lado_03 < lado_01+lado_02:
    if lado_01 == lado_02 == lado_03:
        print("A forma é um triangulo equilátero!")
    elif lado_01 != lado_02 != lado_03 != lado_01:
        print("A forma é um triangulo escaleno!")
    else:
        print("A forma é um triangulo isósceles!")
else:
    print("A forma não é um triangulo!")"""

#EXERCICIO 08
"""idade = int(input("Insira a idade do cliente: "))
renda = float(input("Insira a renda do cliente: "))

if idade >= 18:
    if renda >= 1500:
        situacao = f"O empréstimo foi aprovado, por conta do cliente ser maior de 18 anos e ter uma renda acima ou igual a R$ 1500"
    else:
        situacao = f"O empréstimo foi reprovado, por conta do cliente ser menor de 18 anos e ter uma renda abaixo de R$ 1500"
    print(situacao)
elif idade < 18:
    if renda >= 1000:
        situacao = f"O empréstimo foi aprovado, por conta do cliente ser maior de 18 anos e ter uma renda acima ou igual a R$ 1000"
    else:
        situacao = f"O empréstimo foi reprovado, por conta do cliente ser menor de 18 anos e ter uma renda abaixo de R$ 1000"
    print(situacao)"""

#EXERCICIO 09
escolha = input("Digite a opção que você deseja jogar:" + "\nPedra \nPapel \nTesoura \n").upper()
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
opcoes_maquina = random.choice(opcoes)

if escolha == opcoes_maquina:
    print(f"Você escolheu {escolha} e a maquina escolheu {opcoes_maquina}")
    print("EMPATE")
elif (escolha == "PEDRA" and opcoes_maquina == "TESOURA") or (escolha == "PAPEL" and opcoes_maquina == "PEDRA") or (escolha == "TESOURA" and opcoes_maquina == "PAPEL"):
    print(f"Você escolheu {escolha} e a maquina escolheu {opcoes_maquina}")
    print("Parabéns, você ganhou!")
elif (escolha == "TESOURA" and opcoes_maquina == "PEDRA") or (escolha == "PEDRA" and opcoes_maquina == "PAPEL") or (escolha == "PAPEL" and opcoes_maquina == "TESOURA"):
    print(f"Você escolheu {escolha} e a maquina escolheu {opcoes_maquina}")
    print("Você perdeu!")
else:
    print("Opção Inválida!")
