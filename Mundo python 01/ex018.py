from math import cos, sin, tan, radians

angulo = float(input('Digite o angulo que você deseja: '))

cos = cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))

print(f'O valor do seno é: {sen:.2f}\nO valor do consseno é: {cos:.2f}\nO valor da tangente é: {tan:.2f}')