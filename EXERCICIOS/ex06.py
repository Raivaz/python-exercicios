# RETORNA ALGUNS CÁLCULOS COM O NÚMERO
v = int(input('Digite um número: '))
print('O antecessor de {} é {}, e o sucessor é {}'.format(v, v - 1, v + 1))

print('O dobro de {} é {}'.format(v, v * 2))
print('O triplo de {} é {}'.format(v, v * 3))
print('A raiz quadrada de {} é {}'.format(v, v**(1/2)))

# n1 = 6
# n2 = 8

# print((6+8)/2)

# RETORNA CENTÍMETRO DE MILÍMETRO DE METROS

metro = int(input('Digite quantos metros: '))

print('1 metro tem {} centímetro e {} milímetros'.format(metro*100, metro*1000))

# FAZ A CALCULADORA DE UM NÚMERO

numeroCalc = int(input('Digite um número para calcular: '))

contador = 1
while contador <= 10:
    print('{} X {} = {}'.format(contador, numeroCalc, numeroCalc * contador))
    contador+=1

#TRANSFORMA REAL E DÓLAR

reais = float(input('Quantos reais você tem: '))
print('Com {} reais você consegue comprar {:.2f} dólares'.format(reais, reais / 5.01))

#CALCULA A ÁREA DE UMA PAREDE E RETORNA A QUANTIDADE DE LATAS DE TINTAS NECESSÁRIAS PARA PINTAR A PAREDE

altura = int(input('Altura da parede: '))
largura = int(input('Largura da parede: '))

area = altura * largura
lataTinta = area / 2

print('Para pintar uma area de {} metros quadrados você precisará de {} latas de tintas'.format(area, lataTinta))

valorProduto = float(input('Digite o valor do produto: '))
conDesconto = (valorProduto*5)/100

print('{} com 5% de desconto ficaria {}'.format(valorProduto, valorProduto - conDesconto))


#CALCULA SALARIO COM MAIS 15%
salario = float(input('Digite seu salário: '))

quinzePorCento = (salario*15)/100
salarioComAumento = salario + quinzePorCento

print('O seu salário de {} com 15% de aumento que representa {} ficaria em {}'.format(salario, quinzePorCento, salarioComAumento))