#EXERCÍCIO 10 - CALCULADORA DE FAHRENHEIT
#PEDE O VALOR AO USUÁRIO
celcius = float(input("Insira a temperatura em graus: "))

#CONVERSÃO DO VALOR
fahrenheit = (celcius * (9/5)) + 32

#IMPRESSÃO RESULTADO
print(f"O valor convertido de {celcius}°C é {fahrenheit}°F")
