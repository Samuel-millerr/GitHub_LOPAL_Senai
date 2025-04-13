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


