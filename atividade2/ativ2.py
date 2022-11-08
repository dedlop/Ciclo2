import math

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a > (b + c):
    print('Não é possível calcular.')
else:
    p = (a + b + c) / 2
    Area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'A área do triângulo é {Area:.2f} cm².')