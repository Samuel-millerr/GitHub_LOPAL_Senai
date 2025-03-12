#EXERCÍCIO 12 - CALCULO DE MÉDIA PONDERADA
#PEDE AS NOTAS AO USUÁRIO
nota01 = float(input("Insira o valor da primeira nota: "))
peso_nota01 = float(input("Insira o peso da primera nota: "))

nota02 = float(input("\nInsira o valor da segunda nota: "))
peso_nota02 = float(input("Insira o peso da segunda nota: "))

nota03 = float(input("\nInsira o valor da terceira nota: "))
peso_nota03 = float(input("Insira o peso da terceira nota: "))

#CALCULO DA MÉDIA PONDERADA
soma_pesos = peso_nota01 + peso_nota02 + peso_nota03
media_ponderada = ((nota01*peso_nota01) + (nota02*peso_nota02) + (nota03 * peso_nota03))/soma_pesos

#IMPRESSÃO DO RESULTADO
print(f"A média ponderada das notas é de {media_ponderada:.2f}")

