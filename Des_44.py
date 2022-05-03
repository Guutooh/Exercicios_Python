print('{:=^40'.format(' LOJAS SANTOS '))

compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO \n [1] Dinheiro \n [2] à vista no cartão \n [3] 2x no cartão '
      '\n [4] 3x ou mais no cartão')
opcao = int(input('Escolha uma opação: '))

if opcao == 1:
    total = compras - (compras * 10 / 100)
    print(f'Com desconto de 5%, a sua compra de R${compras} ficará: R${total:.2f}')
elif opcao == 2:
    total = compras - (compras * 5 / 100)
    print(f'Com desconto de 5%, a sua compra de R${compras} ficará: R${total:.2f}')

elif opcao == 3:
    parcelado = compras / 2
    print(f'Sua compra será parcelada em 2x de {parcelado:.2f}')
    print(f'O total de suas compras ficará: R${compras:.2f}')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = compras + (compras * 20) / 100
    parcelado = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de {parcelado:.2f} com juros')
    print(f'Com acrescimos de 20%, a sua compra de R${compras} ficará: R${total:.2f}')

else:
    print('Escolha uma opção Inválida!')
