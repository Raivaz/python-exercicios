#CALCULA A ÁREA DE UMA PAREDE E RETORNA A QUANTIDADE DE LATAS DE TINTAS NECESSÁRIAS PARA PINTAR A PAREDE

altura = int(input('Altura da parede: '))
largura = int(input('Largura da parede: '))

area = altura * largura
lataTinta = area / 2

print('Para pintar uma parede com área de {} metros quadrados você precisará de {} latas de tintas'.format(area, lataTinta))