# frutas = ['banana', 'maça', 'pessego']
# for fruta in frutas:
#     print(fruta)

# mensagem = "samuel"
# for caractere in mensagem:
#     print(caractere)

# tamanhos = ("grande", "pequeno", "médio", "extragrande")
# for tamanho in tamanhos:
#     print("Tamanho: ",tamanho)

# pessoa = {
#     "nome": "",
#     "idade": "",
#     "profissão": "",
#     "numero": "",
#
# }
# print(pessoa["nome"])
#
# for chave, valor in pessoa.items():
#     if chave == "numero":
#         valor = input("Insira o numero: ")
#         print(f"{chave}, {valor}")
#
#     if chave == "idade":
#         valor = input("Insira a idade: ")
#         print(f"{chave}, {valor}")

# alunos = {
#     "123": {
#         "nome": "Maria",
#         "idade": 17},
#
#     "456": {
#         "nome": "Samuel",
#         "idade": 18}
# }
# for id, dados in alunos.items():
#     print(f"\nRA: ",id)
#     for chave, valor in dados.items():
#         print(f"{chave.capitalize()}: {valor}")

# animais = {"gato", "cachorro", "elefante", "girafa"}
# for animal in animais:
#     print("Animal: ", animal)
#     break

# for numero in range(10):
#     print(numero)
# for numero in range(1, 11):
#     print(numero)
# for numero in range(1, 11, 2):
#     print(numero)
# for numero in range(1, 11, 3):
#     print(numero)

nome_do_arquivo = "C:/Users/10082928690/Desktop/teste.txt"
with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())