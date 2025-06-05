import smtplib
import csv
from email.message import EmailMessage

# Função para realizar a leitura dos dados em csv
def ler_csv(arquivo_csv):
    with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for indice, linha in enumerate(reader):
            if indice == 1: # Verifica a primeira linha do arquivo csv (ultima data adicionada)
                dados_dia = linha

    # Atribui o índice da linha csv a variável dados
    dados = (f"Data: {dados_dia[0]}\n"
            f"Horário: {dados_dia[1]}\n"
            f"Esteira01: {dados_dia[2]}\n"
            f"Esteira02: {dados_dia[3]}\n"
            f"Esteira03: {dados_dia[4]}\n")
    return dados

servidor_email = smtplib.SMTP('smtp.gmail.com', 587) # Estabelece uma conexão com o servidor utilizado, nesse caso o gmail
servidor_email.starttls() # Habilita a comunicação

servidor_email.login('mukamiller11@gmail.com','nlii bpog zylb bima') # Loga através da senha de app no e-mail do remetente

# Define o remetente e o destinatário através do endereço de email
remetente = "mukamiller11@gmail.com"
destinatario = ["samuel.m.soares10@aluno.senai.br"]

# Chamada da função para ler o arquivo .csv
dados = ler_csv("arquivoCsv.csv")

# Define o assunto e o corpo do e-mail a ser enviado
assunto = "Relátorio Diário de Estoque"
corpo = f"Olá, tudo bem? Segue abaixo o relatório de estoque diário.\n{dados}"

# Atribui as variáveis declaradas na função aos atributos da biblioteca
msg = EmailMessage()
msg['Subject'] = assunto
msg["To"] = destinatario
msg.add_alternative(corpo)

servidor_email.send_message(msg)

servidor_email.quit()