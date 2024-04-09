# FAZ A CALCULADORA DE UM NÚMERO

numeroCalc = int(input('Digite um número para calcular: '))

contador = 1
while contador <= 10:
    print('{} X {} = {}'.format(contador, numeroCalc, numeroCalc * contador))
    contador+=1