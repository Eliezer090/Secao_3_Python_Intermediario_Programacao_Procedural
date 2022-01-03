#Funcao normal
def func(x,y):
    return x*y
print(func(1,2))

#Funcao lambda
a= lambda x,y:x*y
print(a(2,2))

#Exemplo de onde usariamos isso
lista=[
    ['P1',13],
    ['P3',6],
    ['P4',7],
    ['P7',50],
    ['P2',8]
]

#Ordena, isso nao funciona
lista.sort()
print(lista)
#Isso funciona para ordenar
lista.sort(key=lambda item:item[1])
print(lista)

#isso tambem funciona
print(sorted(lista,key=lambda i:i[1]))
#ordena pelo nome
print(sorted(lista,key=lambda i:i[0]))







