numero = int(input('Digite um numero inteiro: '))
print('Escolha um das bases para conversão:\n [1] Binario \n [2] Octal \n [3] Hexadecimal')
opcao = int(input('Digite sua opção: '))
print()
if opcao == 1:
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Digite uma opção valida')
