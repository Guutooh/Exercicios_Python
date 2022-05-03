primeiro = float(input('Digite o primeiro valor: '))
segundo = float(input('Digite o segundo valor: '))
terceiro = float(input('Digite o terceiro valor: '))

maior = primeiro

if primeiro > segundo and primeiro > terceiro:
    print('O maior número digitado foi {} '.format(primeiro))

elif segundo > primeiro and segundo > terceiro:
    print('O maior número digitado foi {} '.format(segundo))
else:
    print('O maior número digitado foi {} '.format(terceiro))

menor = primeiro

if primeiro < segundo and primeiro < terceiro:
    print('O menor número digitado foi {} '.format(primeiro))

elif segundo < primeiro and segundo < terceiro:
    print('O menor número digitado foi {} '.format(segundo))
else:
    print('O menor número digitado foi {} '.format(terceiro))
