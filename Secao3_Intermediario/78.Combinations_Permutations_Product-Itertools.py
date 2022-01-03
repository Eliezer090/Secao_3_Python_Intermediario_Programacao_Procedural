from itertools import combinations,permutations,product

pessoas = ['Luiz','Andre','eduardo','leticia','fabricio','Rose']
#Agrupa a lista de 2 em 2, não importa a ordem
for grupo in combinations(pessoas,2):
    print(grupo)
print('Permutations:')
#Agrupa a lista de 2 em 2, aqui a ordem importa
for grupo in permutations(pessoas,2):
    print(grupo)

print('Product:')
#Agrupa a lista de 2 em 2, aqui a ordem importa, e junta o elemento com ele mesmo
for grupo in product(pessoas,repeat=2):
    print(grupo)