termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('Pausa.')
    mais = int(input('Quantos temos você quer mostrar mais? [0] para sair. '))

print(f'Progressão finalizada com {total} termos apresentados')
