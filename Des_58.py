from random import randrange
from time import sleep

sorteado = randrange(0, 11)

print('-=' * 20)
print('Adivinhe qual o número entre 0 e 10.')
print('-=' * 20)

acertou = False
tentativas = 0

while not acertou:
    numero = int(input('Adivinhe qual o número: '))
    tentativas += 1
    if numero == sorteado:
        acertou = True
    else:
        if numero < sorteado:
            print('Errou, é um número maior')
        else:
            print('Errou, é um número Menor')
print(f'O número sorteado foi {sorteado} , Você acertou com {tentativas} tentativas')




