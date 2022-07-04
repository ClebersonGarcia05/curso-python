""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário 
com as seguintes informações:  

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Acione também as docstrings da função."""

def notas():
    """ ->  Calcula a quantidade de notas,
    a maior nota, a menor nota, a média da turma
    e a situação (opcional)"""
    dicio = {}
    notas = []
    cont = soma = 0
    while True:
        nota = float(input('Digite a nota: '))
        cont += 1
        soma += nota
        notas.append(nota)
        r = str(input('Quer continuar? ')).strip().upper()[0]
        while r not in 'SN':
            r = str(input('Opção inválida, quer continuar? ')).strip().upper()[0]
        if r == 'N':
            break
    msg = str(input('Deseja ver sua situação?').strip().upper()[0])
    if msg == 'S':
        situação = 'True'
    else:
        situação = 'False'
    dicio['qtd notas'] = cont
    dicio['média da turma'] = soma / cont
    dicio['maior nota'] = max(notas)
    dicio['menor nota'] = min(notas)
    if situação == 'True':
        if dicio['média da turma'] >= 7:
            dicio['situação'] = 'Boa'
        elif dicio['média da turma'] >= 5:
            dicio['situação'] = 'Razoável'
        else:
            dicio['situação'] = 'Ruim'
    return dicio
dicio = notas()
print(dicio)