
l1= [1,2,3,4,5,6,7,8,9]
l2= [variavel for variavel in l1]
print(l2)
l3= [v*2 for v in l1]
print(l3)
l4= [(v,v2) for v in l1 for v2 in range(3)]
print(l4)

l5 = ['luiz','mario','maria']
l6= [v.replace('a','@') for v in l5]
print(l6)

tupla = (
    ('chave','valor'),
    ('chave2','valor2'),
    ('chave3','valor3'),
    ('chave4','valor4'),
)
l7 = [(y,x) for x,y in tupla]
print(l7)

l8 = list(range(100))
l9 = [v for v in l8 if v%2 ==0]
print(l9)
l9 = [v for v in l8 if v%3 ==0 if v%8 ==0]
print(l9)
#com else
l9 = [v if v%3 ==0 else 0 for v in l8 ]
print(l9)

l9 = [v if v%3 ==0 and v%8==0 else 0 for v in l8 ]
print(l9)







