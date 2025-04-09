print("====================")
print("EXERCÍCIO 02 - SENHA")
print("====================\n")

senha = input("Defina a senha a ser utilizada: ")

# LAÇO DE VERIFICAÇÃO DE SENHA
while True:
    i = 0
    i +=1
    senha_digitada = input(f"\nInsira sua {i}° tentativa: ")
    if senha_digitada == senha:
        print("SENHA CORRETA!")
        break
    print("SENHA INCORRETA!")