xml_str = """<config>
    <versao>1.1</versao>
</config>"""

with open ("meu_arquivo.xml","w") as arquivo:
    arquivo.write(xml_str)

with open ("meu_arquivo.xml","r") as arquivo:
    print(arquivo.read())