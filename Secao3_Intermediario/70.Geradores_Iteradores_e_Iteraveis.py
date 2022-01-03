#Interavel
lista=[1,2,3]
print(hasattr(lista, '__iter__')) #é iteravel
lista = '123'
print(hasattr(lista, '__iter__')) #é iteravel
lista= 123
print(hasattr(lista, '__iter__')) #não é iteravel

print('-----iterador------')
#Interador
lista=[1,2,3]

for v in lista: #isto tora a lista uma interavel, mas ela por si nao é interavel
    pass
print(hasattr(lista,'__next__'))
lista= iter(lista)
print(hasattr(lista,'__next__'))

'''--------------------------------------------------------------------------------------------------------'''
print('-----GERADORES---')
import sys
import time
list = list(range(100))
#pega o tamnho dessa lista em bytes
print(sys.getsizeof(list))

"""
Gerador é uma função que ao processando já vai retornando seu valor nao precisa esperar acabar o processamento para retornar
    ele já vai retornando, para isso precisamos botar o yield.
O gerador só vai retornar e salvar na memoria quando pedirmos, com for ou next
"""
#Montando um gerador
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g=gera()

print(g)
#for v in g:
#   print(v)

def gera2():
    var = 'val 1'
    yield var
    var = 'val 2'
    yield var
    var = 'val 3'
    yield var

g = gera2()
#Podemos tanto usar o next quanto o for

print(next(g))

for v in g:
    print(f'for: {v}')

print('----MEMORIA----')

#Memoria
        #list(range(10000)) #isso é a mesma coisa do que a de baixo
l1 = [x for x in range(10)]
print(type(l1))
print(sys.getsizeof(l1))
#Criando do formato gerador, verá que tem o tamanho bem menor
l2 = (x for x in range(10))
print(type(l2))
print(sys.getsizeof(l2))

"""
Aqui da para ver bem a diferença entre usar ou nao os geradores, a lista 2(l2) sempre vai ter o 112 independente do tamanho dela
    pq ela retorna um por vez,  já a lista 1(l1) terá o tamnaho de acordo com os dados que vem o tamanho final no caso.
"""

print('---LISTA 1---')
for v in l1:
    print(sys.getsizeof(l1))
    print(v)
print('---LISTA 2---')
for v in l2:
    print(sys.getsizeof(l2))
    print(v)

#irá manter os 112 de tamanho.
l2 = (x for x in range(10000))
print(type(l2))
print(sys.getsizeof(l2))