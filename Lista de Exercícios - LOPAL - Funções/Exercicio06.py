# Exercício 06

def contar_vogais(palavra):
    qtd_a, qtd_e, qtd_i, qtd_o, qtd_u = 0, 0, 0, 0, 0

    for letra in palavra.lower():
        if letra == "a":
            qtd_a += 1
        elif letra == "e":
            qtd_e += 1
        elif letra == "i":
            qtd_i += 1
        elif letra == "o":
            qtd_o += 1
        elif letra == "u":
            qtd_u += 1
    soma_vogais = qtd_a+qtd_e+qtd_i+qtd_o+qtd_u

    exibir_contagem = {
        "Quantidade de Vogais: ": soma_vogais,
        "Letra A: ": qtd_a,
        "Letra E: ": qtd_e,
        "Letra I: ": qtd_i,
        "Letra O: ": qtd_o,
        "Letra U: ": qtd_u
    }
    return exibir_contagem

print(f"{"="*5} Exercício 06 - Contar Vogais {"="*5}")
print("Insira a suva palavra para realizarmos a contagem de vogais: ")
texto = input(" > ")

print("\nSegue abaixo a contagem sobre a palavra/frase digitada: ")
contagem = contar_vogais(texto)
for chave, valor in contagem.items():
    print(chave, valor)