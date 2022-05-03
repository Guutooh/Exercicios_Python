import random

primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')

nomes = [primeiro, segundo, terceiro, quarto]

random.shuffle(nomes)

print('A ordem de apresentação sera: ', nomes)














