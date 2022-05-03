# termo = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = termo + (10 - 1) * razao
#
# for c in range(termo, decimo + razao, razao):
#     print(c, end='-> ')
# print('Acabou')


termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

#termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('Fim.')
