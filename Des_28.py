import random
import time
import termcolor



#sorteado = random.randint(0,5)
sorteado = random.randrange(0, 5)
print('-=' * 20)
print('Adivinhe qual o número entre 0 e 5.')
print('-=' * 20)

numero = int(input('Adivinhe qual o número: '))
print('Processando...')
time.sleep(2)

if numero == sorteado:
    print(f'O número sorteado foi {sorteado} , Você acertou!')
else:
    #add módulo chamando cprint, passando o texto em seguida a cor
    termcolor.cprint(f'Você perdeu, O número sorteado foi {sorteado}', 'red')









