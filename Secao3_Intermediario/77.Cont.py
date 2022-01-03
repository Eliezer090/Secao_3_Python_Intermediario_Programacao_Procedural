from itertools import count

#retorna infinito cuidado
contador = count(start=1,step=0.1)
for valor in contador:
    print(round(valor,3))
    if valor >=10:
        break

#Começa de um valor e vai diminuindo um
contador = count(start=9,step=-1)
for valor in contador:
    print(valor)
    if valor >=10 or valor <= -10:
        break
#Colocare um indice para uma lista
contador = count()
lista=['maria','joao','eduardo']
lista = zip(contador,lista)
print(list(lista))

