dias = int(input('Por quantos dias foi alugado: '))
km = float(input('Quantos km você rodou: '))

teste = 'teste5'


total = (dias * 60) + (km * 0.15)

print('O valor a pagar é R${}'.format(total))