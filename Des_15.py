dias = int(input('Quantos dias alugados? '))
km = int(input('Informe quantos KM percorridos: '))

preco = (dias * 60) + (km * 0.15)
custo_km = km * 0.15
custo_dias = dias * 60

print('O total a pagar é de R${:.2f}, sendo R${:.2f} de aluguel '
      'e R${} de KM rodados '.format(preco, custo_dias, custo_km))
