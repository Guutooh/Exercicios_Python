import math
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipotenuza = math.hypot(oposto, adjacente)

print('Valor hipotenuza {:.2f}'.format(hipotenuza))


