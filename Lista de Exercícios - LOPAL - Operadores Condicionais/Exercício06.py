#EXERCÍCIO 06 - VERIFICAÇÃO DE HORA VALIDA
horas = int(input("Insira o valor das horas: "))
minutos = int(input("Insira o valor dos minutos: "))
segundos = int(input("Insira o valor dos segundos: "))

if 0 <= horas < 24 and 0 <= minutos < 60 and 0 <= segundos < 60:
    print(f"A hora {horas:02d}:{minutos:02d}:{segundos:02d} é valida!")
else:
    print(f"A hora {horas:02d}:{minutos:02d}:{segundos:02d} não é valida!")
