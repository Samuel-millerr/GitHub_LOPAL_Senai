# Exercício 03
print(f"{"="*5} Exercício 02 - Conversor de Temperatura {"="*5}")

def converter_celsius_para_fahrenheit(temperatura):
    fahrenheit = temperatura * 1.8 + 32
    return fahrenheit

print("Bem vindo(a) ao conversor de temperatura de Celsius ----> Fahrenheit!")
print("Insira a temperatura em Celsius para realizar a conversão")
celsius = float(input(" > "))

