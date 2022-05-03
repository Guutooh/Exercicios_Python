largura = float(input('Informe a largura da parede: '))
altura = float(input('agora, informe a altura: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.1f}l de tinta' .format(tinta))
