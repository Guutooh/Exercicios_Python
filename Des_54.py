import datetime

atual = datetime.date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Existem {maior} pessoas maior de idade \nE {menor} pessoas menor de idade')
