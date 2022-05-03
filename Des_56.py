somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulher = 0
for a in range(1, 5):
    print(f'Nome da {a}ªPessoa')
    nome = input('Nome:')
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ')

    somaIdade += idade

    if a == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'fF' and idade < 20:
        mulher += 1
mediaIdade = somaIdade / 4
print(f'A media de idade do grupo é de {mediaIdade} anos')
print(f'O Homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')
