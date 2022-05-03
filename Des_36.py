valor_imovel = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento? '))
parcelas = valor_imovel / (anos_financiamento * 12)
minimo = salario * 30 / 100

if parcelas >= minimo:
    print(f'Para pagar uma casa de R${valor_imovel:.2f} em {anos_financiamento} a prestação sera de R${parcelas:.2f} \n'
          f'Emprestimo \033[1;31mNEGADO!\033[m')
else:
    print(f'Para pagar uma casa de R${valor_imovel:.2f} em {anos_financiamento} a prestação sera de R${parcelas:.2f} \n'
          f'Emprestimo \033[1;32mCONCEDIDO!\033[m')


