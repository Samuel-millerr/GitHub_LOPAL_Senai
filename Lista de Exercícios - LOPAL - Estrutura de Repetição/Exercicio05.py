print("===========================")
print("EXERCÍCIO 05 - 3 TENTATIVAS")
print("===========================\n")

senha = "python123"
tentativas = 3
while tentativas >= 0:
    senha_digitada = input("Digite a senha: ").strip()

    if senha == senha_digitada:
        print("SENHA CORRETA! Acesso liberado.")
        break
    elif tentativas == 1:
        print("ACESSO BLOQUEADO! Todas as tentativas foram utilizadas.")
        break
    else:
        tentativas -= 1
        print(f"ACESSO NEGADO! {tentativas} tentativas restantes.")

