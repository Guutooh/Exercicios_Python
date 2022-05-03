import datetime
ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))
idade = datetime.date.today().year - ano_nascimento
print(f'O atleta possui {idade} anos')

if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
