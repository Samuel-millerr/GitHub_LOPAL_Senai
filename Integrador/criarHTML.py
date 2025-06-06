import csv

# Função para identificar qual o status da esteira
def emoji(valor):
    legenda = {
        "0": "⚪",
        "1": "🔴",
        "2": "🟡",
        "3": "🟢"
    }
    return legenda.get(valor)

# Função para ler e pegar os dados do arquivo csv
def ler_csv(arquivo_csv):
    dados_csv = []
    with open(arquivo_csv, "r", encoding="utf-8") as arquivo:  # Abre o arquivo .csv
        reader = csv.DictReader(arquivo)  # Realiza a leitura do mesmo
        for i in reader:
            dados_csv.append({
                "data": i["Date"],
                "horario": i['Time'],
                "esteira01":  i["esteira1"],
                "esteira02": i["esteira2"],
                "esteira03": i["esteira3"]
            }) # Estrutura os dados das linhas em um dicionário e adiciona os dados de cada linhas do csv em uma lista
    return dados_csv

# Função para gerar o código html com os dados do csv
def gerar_html(dados, nome_arquivo = "index.html"):
    with open(nome_arquivo, 'w', encoding="utf-8") as index: # Criação da página html

        # Estruturação do código da página, a cada "write" o código html abaixo está sendo implementado no arquivo criado
        index.write("""
        <html>
        <head>
            <title> Status das Esteiras - Monitoramento de Estoque </title>
        </head>
        <body>
            <style>
                th, td{
                    border: 2px solid black;
                    padding: 2px;
                    text-align: center;
                }
            </style>
        
            <h1> Status das Esteiras - Monitoramento de Estoque </h1>
            <table style="width:70%">
                <tr>
                    <th>Data</th>
                    <th>Horário</th>
                    <th>Esteira01</th>
                    <th>Esteira02</th>
                    <th>Esteira03</th>       
                </tr> 
        """)

        # For usado para pegar os dados de cada linha e os inserir em uma tabela no arquivo html
        for dado in dados:
            # Chamada da função emoji, para identificação dos status das esteiras
            e1 = emoji(dado["esteira01"]) + " " + dado["esteira01"]
            e2 = emoji(dado["esteira02"]) + " " + dado["esteira02"]
            e3 = emoji(dado["esteira03"]) + " " + dado["esteira03"]

            index.write(f"""
            <tr>
                <td>{dado["data"]}</td>
                <td>{dado["horario"]}</td>
                <td>{e1}</td>
                <td>{e2}</td>
                <td>{e3}</td>
            </tr>
            """)

        index.write(f"""
            </table>
        </body>
        </html>
        """)

# Chamada das funções com os parâmetros necessários
dados_csv = ler_csv("arquivoCsv.csv")
gerar_html(dados_csv)