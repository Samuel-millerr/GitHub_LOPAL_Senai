print("====================")
print("EXERCÍCIO 02 - SENHA")
print("====================\n")

senha = input("Defina a senha a ser utilizada: ").strip()

# LAÇO DE VERIFICAÇÃO DE SENHA
i = 0
while True:
    i +=1
    senha_digitada = input(f"\nInsira sua {i}° tentativa: ").strip()
    if senha_digitada == senha:
        print("SENHA CORRETA!")
        break
    print("SENHA INCORRETA!")