altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso:'))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.1f}: Abaixo do peso.')
elif imc <= 25:
    print(f'Seu imc é de {imc:.1f}: Peso ideal.')
elif imc < 30:
    print(f'Seu imc é de {imc:.1f}: Sobrepeso.')
elif imc <= 40:
    print(f'Seu imc é de {imc:.1f}: Obesidade.')
else:
    print('Obesidade móbida, Cuidado!')
