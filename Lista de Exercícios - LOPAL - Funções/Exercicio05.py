# Exercício 05

def eh_primo(num):
    primo = False
    for i in range(2, num):
        if num == 1:
            primo = False
        elif num % i == 0:
            primo = False
            break
        else:
            primo = True
    return primo

print(f"{"="*5} Exercício 05 - Verificador de Número Primo {"="*5}")
print("Olá, insira algum número para o programa verificar se ele é primo ou não.")
numero = int(input(" > "))

ehPrimo = eh_primo(numero)
print(f"O número {numero} é primo? {ehPrimo}")
