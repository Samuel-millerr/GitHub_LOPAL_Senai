import smtplib
import csv

servidor_email = smtplib.SMTP('smtp.gmail.com', 587) # Estabelece uma conexão com o servidor utilizado, nesse caso o gmail

servidor_email.starttls() # Habilita a comunicação
servidor_email.login('mukamiller11@gmail.com','nlii bpog zylb bima')

remetente = "mukamiller11@gmail.com"
destinatario = ["alex.l.pinheiro@aluno.senai.br"]

with open("arquivoCsv.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.reader(arquivo)
    for indice, linha in enumerate(reader):
        if indice == 1:
            dadosDia = linha

            data = dadosDia[0]
            horario = dadosDia[1]
            horario1 = horario[0:2] + ";" + horario[3:5] + ";" + horario[6:]
            esteira01 = dadosDia[2]
            esteira02 = dadosDia[3]
            esteira03 = dadosDia[4]

print(horario1)
conteudo = ("Olá, segue abaixo o relatório diário:\n"
            f"Data; {data}\n"
            f"Esteira01; {esteira01}\n"
            f"Esteira02; {esteira02}\n"
            f"Esteira03; {esteira03}\n")

servidor_email.sendmail(remetente, destinatario, conteudo)


servidor_email.quit()