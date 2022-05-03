produto = float(input('Entre com preço do produto: '))
desconto = (produto * 5 / 100)
total = produto - desconto

print('O valor do produto de R${:.2f} com desconto de 5%, teve desconto de R${:.2f},'
      ' ficando com valor total de R${:.2f}'.format(produto, desconto, total))
