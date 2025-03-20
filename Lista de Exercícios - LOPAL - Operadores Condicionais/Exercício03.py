#EXERCÍCIO 03 - CALCULADORA DE DESCONTO DE PRODUTO
qtd_produto = int(input("Digite a quantidade de produtos: "))
valor_produto = float(input("Digite o valor unitário de cada produto: "))
valor_total = qtd_produto * valor_produto

if qtd_produto >= 100:
    desconto = valor_total * 0.1
else:
    desconto = valor_total * 0.05

produto_descontado = valor_total - desconto
print("Segue abaixo as informações do produto:")
print(f"Preço Inicial: R${valor_produto:.1f} \nQuantidade: {qtd_produto} \nDesconto por Unidade: R${desconto / qtd_produto:.1f} \nValor Final: R${produto_descontado:.1f}")
