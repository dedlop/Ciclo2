a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b and a < c:
    print('O menor valor é: ', a)
elif b < c:
    print('O menor valor é: ', b)
else:
    print('O menor valor é: ', c)