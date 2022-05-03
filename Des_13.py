
salario = float(input('Qual é o salario do funcionário? R$'))
reajuste = float(input('Informe qual a porcentagem de reajuste: '))
novo_salario = float(salario + (salario*reajuste/100))

print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, '
      'passa a receber R${:.2f}'.format(salario, reajuste, novo_salario))
