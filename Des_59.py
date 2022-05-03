primeiro = float(input('Primeiro valor> '))
segundo = float(input('Primeiro valor> '))

print('[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')

escolha = 0

while escolha != 5:
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print(f'A soma dos números é: {primeiro + segundo}')
    elif escolha == 2:
        print(f'Os valores multiplicados são: {primeiro * segundo}')
    elif escolha == 3:
        if primeiro > segundo:
            print(f'O maior valor é: {primeiro}')
        else:
            print(f'O maior valor é: {segundo}')
    elif escolha == 4:
        primeiro = float(input('Primeiro valor> '))
        segundo = float(input('Primeiro valor> '))
    elif escolha == 5:
        print('Fim do programa! ')
