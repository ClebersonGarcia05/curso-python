'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pause de 1 segundo entre eles'''

from time import sleep
import emoji


for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emoji.emojize('BOOM :boom: BOOM :fireworks: BOOM :boom: POW:fireworks: :boom:', language='alias'))