
sexo = input('Informe seu sexo: [M/F]: ').strip().upper()[0]

while sexo != 'M' and sexo != 'F':
#while sexo not in 'MmfF':
    print('Sexo inválido!')
    sexo = input('Digite um sexo válido: ')
else:
    print('Obrigado pela informação correta: ')
