from itertools import groupby,tee

alunos = [
    {
        'nome': 'Luiz',
        'nota': 'A',
    },
    {
        'nome': 'Leticia',
        'nota': 'B',
    },
    {
        'nome': 'Fabricio',
        'nota': 'C',
    },
    {
        'nome': 'Joao',
        'nota': 'B',
    },
    {
        'nome': 'Eduardo',
        'nota': 'A',
    }, {
        'nome': 'André',
        'nota': 'C',
    }
, {
        'nome': 'André',
        'nota': 'C',
    }
    , {
        'nome': 'André',
        'nota': 'D',
    }

]
ordena = lambda item: item['nota']
#Ordenado
alunos.sort(key=ordena)
for aluno in alunos:
    print(aluno)

#Agrupa
print('groupby:')
#Este sort é importante pois ele ordena nossos valores sem ele fica tudo errado
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamneto, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamneto}')
    #O tee serve meio que para fazer uma cópia desses valores, pois se tentarmos usar o valores_agrupados ele vai ter
    # esgotado no for se usarmos depois ele mostra sempre 0
    va1, va2 = tee(valores_agrupados)
    for aluno in va1:
        print(f'Alunos: {aluno}')

    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram a nota {agrupamneto}')
