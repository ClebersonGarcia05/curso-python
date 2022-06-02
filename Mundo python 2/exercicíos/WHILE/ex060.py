""" Faça um programa que leia um número e mostre o seu fatorial
EX: 5! = 5x4x3x2x1 = 120 """

arm = 1
fat = 1
num = int(input('Digite um número para saber o fatorial: '))
esc = num
""" for i in range(num, -1, -1):
    if i > 0:
        soma *= i
print(soma) """

while arm > 0:
    arm = num
    fat *= num
    arm -= 1
    num -= 1
print(f'O fatorial do número {esc} é: {fat}')