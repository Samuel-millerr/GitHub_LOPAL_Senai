alfabeto = "abcdefghijklmnopqrstuvwxyz"

with open ("criptografado.txt", "r", encoding="utf-8") as arquivo:
    frase = arquivo.read()

for letra in frase:
    posicao = alfabeto.find(letra)
    if posicao != -1:
        posicao_normal = posicao - 3
        print(alfabeto[posicao_normal], end="")
    elif alfabeto[posicao] == "z":
        print(" ", end="")