# from math import factorial
#
# numero = int(input('Digite um  número para calcular sua fatorial: '))
# fatorial = factorial(numero)
#
# print(f'O fatorial de {numero} é {fatorial}')

#######################################################################

numero = int(input('Digite um  número para calcular sua fatorial: '))
contador = numero
fatorial = 1

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)



