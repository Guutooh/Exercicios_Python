frase = input('Digite uma frase: ')
palindromo = frase.replace(" ", "").upper()
inverso = palindromo.replace(" ", "").upper()

for c in frase:
    if palindromo == inverso[::-1]:
        print(f'A frase - {frase} \né palindromo')
        break
    else:
        (print(f'A frase - {frase} \nNão é um palíndromo!'))
        break
