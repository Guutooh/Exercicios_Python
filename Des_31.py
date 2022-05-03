distancia = float(input('Informe a distancia da viagem em Km: '))
if distancia > 200:
    custo = distancia * 0.45
else:
    custo = distancia * 0.50
print('O preço da passagem é R${:.2f}'.format(custo))
