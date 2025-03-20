#EXERCÍCIO 09 - DIVISÃO
#PEDE O DIVISOR E O DIVIDENDO AO USUÁRIO
dividendo = float(input("Insira o dividendo: "))
divisor = float(input("Insira o divisor: "))

#CALCULO DA DIVISÃO
quociente = dividendo / divisor
resto = dividendo % divisor

print(f"Segue abaixo as informações de toda a divisão:")
print(f"Dividendo: {dividendo:.1f}\nDivisor: {divisor:.1f}\nQuociente/resultado: {quociente:.1f}\nResto: {resto:.1f}")

