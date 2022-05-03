nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 5:
    print(f'O aluno que tirou {nota1} e {nota2} sua média é {media:.1f}, aluno \033[1;31mREPROVADO\033[m')
elif media < 6.9:
    print(f'O aluno que tirou {nota1} e {nota2} sua média é {media:.1f}, aluno \033[1;94mRECUPERAÇÃO\033[m')
else:
    print(f'O aluno que tirou {nota1} e {nota2} sua média é {media:.1f}, aluno \033[1;32mAPROVADO\033[m')
