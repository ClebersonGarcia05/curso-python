""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador. """

jog = {}
time = []
gols = []
while True:
    jog['nome'] = str(input('Digite o nome do jogador: '))
    part = int(input(f'Digite quantas partidas o {jog["nome"]} jogou: '))
    for i in range(part):
        gols.append(int(input(f'  --  Quantidade de gols feitos na {i+1}º partida: ')))
    jog['gols'] = gols.copy()
    jog['total'] = sum(gols)
    time.append(jog.copy())
    gols.clear()
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('Erro, digite novamente!')
            print()
    if r == 'N':
        break
print(f'{"Nº":^4} {"Nome":<15} {"gols":<15} {"Total":<15}')
for i, j in enumerate(time):
    print(f'{i:^4} ', end='')
    for k, v in j.items():
        print(f'{str(v):<15} ', end='')
    print()
while True:
    part = 0
    n = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if n == 999:
        break
    if n != i:
        print('\033[31mCódigo errado, tente novamente!\033[m')
    for i, v in enumerate(time):
        if n == i:
            print(f'Dados do jogador {v["nome"]}: ')
            for k, nv in v.items():
                if k == 'gols':
                    for l in nv:
                        print(f'  --  No jogo {part+1} fez {l} gols')
                        part += 1  
print('Programa finalizado!')