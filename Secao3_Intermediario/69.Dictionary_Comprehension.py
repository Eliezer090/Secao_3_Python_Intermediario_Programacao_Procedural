
lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]

d1 = {x.upper():y.upper() for x,y in lista}
print(d1)

#Aqui temos um set que nao pode ser alterado.
d1 = {x for x in range(5)}
print(d1, type(d1))

#Aqui sim temos um dict(Dicionario) com chave e valor  o valor elevado a 2
d1 = {f'chave_{x}':x**2 for x in range(5)}
print(d1, type(d1))










