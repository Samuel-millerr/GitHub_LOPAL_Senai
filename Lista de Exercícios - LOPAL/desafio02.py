#DESAFIO 02 - EMPRESTIMO
#PEDE O NÚMERO AO USUÁRIO
capital = float(input("Informe o capital: "))
taxa_juros = float(input("Informe a taxa de juros: "))
tempo_anos = int(input("Informe o tempo, EM ANOS: "))

#CALCULA O MONTANTE
montante = capital * (1+(taxa_juros/100))**tempo_anos

#IMPRIME O RESULTADO
print(f"O valor dos juros é de R$ {montante-capital:.2f} e o montante é R$ {montante:.2f}")


