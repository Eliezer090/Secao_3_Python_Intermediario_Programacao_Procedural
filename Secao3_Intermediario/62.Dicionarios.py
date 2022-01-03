#Maneira 1 de criar
d1 = {'chave1':'valor'}
d1['nova']='valor nova'
print(d1)
print(d1['chave1'])

#Maneira 2 de criar dicionarios
d2 = dict(chave1='valor chave',chave2='valor chave 2')
d2['nova3'] = 'valor nova 3'
print(d2)

d3={
    'str': 'asd',
    123:'aaa',
   (1,2,3,4):'tupla'
}
print(d3[(1,2,3,4)])
#usar get é o melhor
print(d3.get('aa'))
#checando
valor = d3.get('str')
if valor is not None:
    print(valor)

#Excluir
print(d3)
del d3['str']
print(d3)

#checando se existe
print(123 in d3)
#Se existe nas chaves
print(123 in d3.keys())
#Se existe nos valores
print('tupla' in d3.values())

print('-----interando-----')
#interando
for k in d3:
    print(k)

#Valores
for v in d3.values():
    print(v)
#pegando chave e valor
for i in d3.items():
    print(i)
    print(i[1])

print('-------chave e val junto-------')
#chave e valor junto
for k,v in d3.items():
    print(k,v)


#Dicionarios dentro de dicionarios
dicCliente = {
    'Cliente1':{
        'Nome':'Joao',
        'Sobrenome': 'fulano',
    },
    'Cliente2':{
        'Nome':'Maria',
        'Sobrenome': 'Eduarda',
    }
}

for cliente_k,cliente_v in dicCliente.items():
    print(f'{cliente_k}')
    for dados_k,dados_v in cliente_v.items():
        print(f'\t{dados_k}= {dados_v}')

print('----CONVERSAO----')
#Convertendo lista para dicionario
lista=[
    ['chave1',1],
    ['chave2',2],
    ['chave3',3],
]

lista = dict(lista)
print(lista)

#Eliminar uma chave

d1={
    1:2,
    2:3,
    4:5,
    'a':3
}

print(d1)
d1.pop(4)
print(d1)

#Concatenar 2 dicioanrios

d2={
    7:2,
    9:2,
    6:'aa',
    'bb':'oo'
}

d1.update(d2)
print(d1)




