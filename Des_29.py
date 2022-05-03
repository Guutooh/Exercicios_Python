import termcolor

velocidade = int(input('Digite sua velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que, é de 80Km/h '
          'você deve pagar uma multa de \033[1;31mR${}\033[m'.format(multa))
else:
    termcolor.cprint('Tenha um bom dia! Dirija com segurança!', 'yellow')
