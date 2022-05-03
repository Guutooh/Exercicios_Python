import datetime
nascimento = int(input('Insira seu ano de nascimento:'))
atual = datetime.date.today().year
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

if idade == 18:
    print('Você tem que se alistar')
elif idade < 18:
    diferenca = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {diferenca}')
    ano = atual + diferenca
    print(f'seu alistamento será em {ano}')
elif idade > 18:
    diferenca = idade - 18
    print(f'Você já deveria ter se alistado a {diferenca} anos')
    ano = atual - diferenca
    print(f'seu alistamento foi em {ano}')
