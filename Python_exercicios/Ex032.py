#Desafio ano bissexto

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é bissexto.'.format(ano))
else:
    print('Esse ano {} não é bissexto.'.format(ano))