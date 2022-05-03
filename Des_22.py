
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsulo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome ao todo possui {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras  '.format(nome.split()[0], nome.find(' ')))

