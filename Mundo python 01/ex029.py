from random import randint
from cores import cores

velo = randint(0, 200)

if velo >= 80:
    print(f'{cores["vermelho"]}Você estava a uma velocidade de {velo}km\h, e a máxima permitida é de 80km\h')
    print(f'Você foi multado em R${(velo - 80) * 7}')
else:
    print('\033[1;32mSiga sua viagem com cuidado!!!\033[m')