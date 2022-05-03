
frase = input('Digite uma frase: ').strip().lower()
print('A letra A aparece {} na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A útima letra A apareceu na posição {}'.format(frase.rfind('a')+1))
