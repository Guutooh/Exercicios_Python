import datetime
ano = int(input('Qual ano gostaria de analisar? Ou coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('A ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
