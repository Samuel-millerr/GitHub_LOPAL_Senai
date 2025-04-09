print("==========================================")
print("EXERCÍCIO 04 - VERIFICAÇÃO DE NÚMERO PRIMO")
print("==========================================\n")

print("Digite dois números inteiros.")
numero_01 = int(input("Primeiro número: "))
numero_02 = int(input("Segundo número: "))
primo = True

if numero_01 <= 0 or numero_02 <= 0:
    print("Digite um número correto, não exitem números primos negativos.")
else:
    if numero_01 > numero_02:
        numero_01, numero_02 = numero_02, numero_01
    else:
        # VERIFICAÇÃO DE NÚMERO PRIMOS ENTRE OS NÚMEROS ESCOLHIDOS
        for n in range(numero_01+1, numero_02):
            i = 2
            while i < n:
                if n % i == 0:
                    primo = False
                    break

                else:
                    primo = True
                    i += 1

            if primo:
                print(n)

