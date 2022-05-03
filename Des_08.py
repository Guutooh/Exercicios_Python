medida = float(input('Distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
he = medida * 0.01
de = medida * 0.1
print('A Conversão de {}m corresponde a {:.0f}cm | {:.0f}mm | {} Km | {} de | {} he'  .format(medida, cm, mm, km, de,he ))
