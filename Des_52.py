numero = int(input('Digite um numero: '))
cont = 0

for c in range(1, numero + 1):

    if numero % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print(f'\n\033[m O número {numero} foi divisivel {cont} vezes')
if cont == 2:
    print(f'\033[32m Número {numero} é PRIMO \033[m')
else:
    print(f'\033[31m Número {numero} Não é PRIMO \033[m')
