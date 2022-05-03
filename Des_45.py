import random
import time
tipos = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0, 2)
print(f'O computador escolheu {tipos[computador]}')

print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Faça sua escolha:'))

print('Jo')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POOOOO!!!')
time.sleep(1)

print('-=' * 13)
print(f'Computador jogou {tipos[computador]}')
print(f'Jogador jogou {tipos[jogador]}')
print('-=' * 13)

if computador == 0: #pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Ganhou')
    elif jogador == 2:
        print('Jogador Perdeu')
    else:
        print('Opção Invalida')

elif computador == 1: #Papel
    if jogador == 0:
        print('Perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Ganhou')
    else:
        print('Opção invalida')

elif computador == 2: #Tesoura
    if jogador == 0:
        print('Ganhou')
    elif jogador == 1:
        print('Perdeu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção invalida')
