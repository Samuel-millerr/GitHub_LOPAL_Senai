#EXERCÍCIO 03 - VERIFICAÇÃO DE CONDIÇÕES
#PEDE OS VALORES AO USUÁRIO
valor01 = float(input("Insira o primeiro valor: "))
valor02 = float(input("Insira o segundo valor: "))

#COMPARAÇÃO DOS VALORES
comparacao = bool(valor01 >= 3), bool(valor02 <= 4)
print(comparacao)

#IMPRIME O RESULTADO
print(f"\nO {valor01} é maior ou igual que 3 \nO {valor02} é menor ou igual a 4 \nAlguma das condições anterioes é verdadeira? \n{bool(comparacao)} ")