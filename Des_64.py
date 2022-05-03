
numero = 0
contador = 0
soma = 0


numero = float(input('Digite um némro [999 para sair]: '))

while numero != 999:
    soma += numero
    contador += 1
    numero = float(input('Digite um némro [999 para sair]: '))

print(f'Você digitou {contador} números e a soma entre eles foi {soma}')


