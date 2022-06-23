""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador. """

jog = {}
jogadores = []
gols = []
while True:
    jog['nome'] = str(input('Digite o nome do jogador: '))
    part = int(input(f'Digite quantas partidas o {jog["nome"]} jogou: '))
    for i in range(part):
        gols.append(int(input(f'Quantidade de gols feitos na {i+1}º partida: ')))
    jog['gols'] = gols.copy()
    jog['total'] = sum(gols)
    jogadores.append(jog.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('Erro, digite novamente!')
            print()
    if r == 'N':
        break
print('-=' * 30)
print(jogadores)
print('-=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jog["nome"]} jogou {part} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols')