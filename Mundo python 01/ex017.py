import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hi = math.hypot(co, ca)

print(f'A hipotenusa é {hi:.2f}')