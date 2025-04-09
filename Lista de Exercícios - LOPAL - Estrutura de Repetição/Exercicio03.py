print("===================")
print("EXERCÍCIO 03 - MENU")
print("===================\n")

print("AVISO!!! Digite sua opção de escolha somente através do número correspondente a ela.")
escolha = int(input("Gostaria de entrar no menu?\n( 1 ) Sim\n( 0 ) Não\n"))

# LOOP DE SELEÇÃO DO MENU
while escolha == 1:
    escolha = int(input("\nSelecione alguma das opções:\n( 1 ) Continuar no menu\n( 0 ) Sair do menu\n"))
    if escolha == 0:
        break
    elif escolha != 1:
        print("\nEscolha uma opção correta!")
        escolha = 1
    else:
        escolha = 1
print("Obrigado por usar nosso menu!")