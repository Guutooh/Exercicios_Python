salario = float(input('Qual o salario do funcionário: R$'))

if salario <= 1250:
    reajuste = salario + ((salario * 15) / 100)
else:
    reajuste = salario + ((salario * 10) / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, reajuste))
