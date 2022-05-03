soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0

resposta = 'S'
while resposta in 'Ss':
    numero = float(input('Digite um némero: '))

    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = input('Deseja continuar? [S/N]: ').upper().strip()[0]

media = soma / numero

print(f'você digitou {quantidade} números e a media foi {media}')
print(f'O maior número foi {maior} e o menor número foi {menor}')


