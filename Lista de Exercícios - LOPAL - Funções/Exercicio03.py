# Exercício 03

def converter_celsius_para_fahrenheit(temperatura):
    fahrenheit_funcao = temperatura * 1.8 + 32
    return fahrenheit_funcao

print(f"{"="*5} Exercício 03 - Conversor de Temperatura {"="*5}")
print("Bem vindo(a) ao conversor de temperatura de Celsius ----> Fahrenheit!")
print("Insira a temperatura em Celsius para realizar a conversão")
celsius = float(input(" > "))

fahrenheit = converter_celsius_para_fahrenheit(celsius)
print(" °Celsius ----> °Fahrenheit")
print(f" °{celsius:.1f}     ----> °{fahrenheit:.1f}")
