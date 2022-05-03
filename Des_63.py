numero = int(input('Entre com numero para sequência de Fibonacci: '))
print()

pos1 = 0
pos2 = 1
contador = 3

print(f'{pos1} -> {pos2}', end=' -> ')
while contador <= numero:
    pos3 = pos1 + pos2
    print(pos3, end=' -> ')
    pos1 = pos2
    pos2 = pos3
    contador += 1
print(' Fim.')
