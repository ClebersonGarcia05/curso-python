""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort). No final mostre a lista ordenada na tela """

lista = []
for i in range(0, 5):
    v = int(input('Digite um valor: '))
    if i == 0 or v > lista[-1]:
        lista.append(v)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')