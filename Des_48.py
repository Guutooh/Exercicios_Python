contador = 0
volta = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        volta += 1
        contador += contagem
print(f'Todos os {volta} valores deu um total de {contador}')
