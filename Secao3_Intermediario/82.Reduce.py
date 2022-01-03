from dados import produtos,pessoas,lista
from functools import reduce

#Reduce é uma função acumuladora no final de tudo, reduzir a um unico valor.
#Aqui ela está somando o valor da lista valor anterior mais o atual,dps o atual mais o proximo 0+1+2+3....
soma_lista = reduce(lambda ac, i: i+ac,lista,0)
print(soma_lista)

print('Dic_produtos:')

soma_precos = reduce(lambda ac,p:p['preco']+ac,produtos,0)
print(soma_precos)
#Media do preco dos produtos
print(soma_precos/len(produtos))

#Média de idades
print('Média de idades:')
soma_idades = reduce(lambda ac, p:ac+p['idade'],pessoas,0)
print(round(soma_idades/len(pessoas)))



