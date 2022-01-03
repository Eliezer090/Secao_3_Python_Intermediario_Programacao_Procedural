"""
Como unir interaveis
"""
#Associar as 2 listas, precisa estar na ordem., utilizando ZIP
cidades = ['Sao paulo','BH','Salvador']
estados=['SP','MG','BA']

cidades_estados= zip(estados,cidades)

print(cidades_estados)
#Pode ser usado para fazer conversões desta maneira
#print(list(cidades_estados))
#print(dict(cidades_estados))
for v in cidades_estados:
    print(v)

"""
Associar 2 listas com zip_longest, serve para unir as 2 listas mas sem necessidade dos 2 interaveis ter a msm qtde de dados,
    irá preencher com none se nao encontrar.
"""
from itertools import zip_longest, count
indice=count()
cidades = ['Sao paulo','BH','Salvador','Monte belo']
estados=['SP','MG','BA']
cidades_estados= zip_longest(estados,cidades)
#preencher com none
print(list(cidades_estados))

cidades_estados= zip_longest(estados,cidades,fillvalue='estado')
#preencher com estado ao invez de none
#print(list(cidades_estados))
for v in cidades_estados:
    print(v)

#Utilizado zip pois o zip tem fim o zip_longest iria ficar em loop
cidades_estados= zip(indice,estados,cidades)
#preencher com estado ao invez de none
#print(list(cidades_estados))
for indice,estado,cidade in cidades_estados:
    print(indice,estado,cidade)

