#Conjuntos nao tem o par de chave e valor só valores
'''
add (adiciona), update(atualiza),clear,discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symetric_difference ^ (Elementos que estao nos 2 sets mas nao em ambos)
'''
#Criar um novo set
s1= set()
s1.add(1)
s1.add(2)
s1.add((1,2,3,4))
print(s1)

s1.discard(2)
print(s1)
#update interage com cada caractere, e sets nao respeitam ordem sao rebeldes
s1.update('python')
print(s1)
#já o add nao interage
s1.add('python')
print(s1)


#sets nao aceitam elementos duplicados, eles podem ser amplamentes usados para remover elementos suplicados
s2 = set()
#E sim podemos passar isso que sla ele se intende
s2.update([1,2,3],{3,4,5})
print(s2)

#Eliminando repetidos de uma lista  e voltando para lista
l1= [1,2,3,3,3,3,3,5,5,5,5,3,8,'Eliezer']
l1=set(l1)
l1 = list(l1)
print(l1)

s3 = {1,2,3,4,5}
s4= {1,2,3,5,6,7}
#union Ou | fazem a mesma coisa
s5 = s3 | s4
print(s5)
#intersection Ou & fazem a mesma coisa
s5 = s3 & s4
print(s5)
#difference Ou - Vai pegar todos os elementos que nao estejam nos 2 sets mas levando em consideração só o da esqueda
# para fazer a comparação, só o 4 nao está no set da direita
s5 = s3 - s4
print(s5)
s5 = s4 - s3
print(s5)
#symetric_difference Ou ^ Vai pegar os valores dos 2 sets, mas elementos que nao estão nos 2 ao mesmo tempo
s5 = s3 ^ s4
print(s5)

#Verificar se as listas sao iguais utilizando set mesmo que esteja forra de ordem
l1 = ['MARIA', 'JOAO','PEDRO']
l2 = ['MARIA', 'PEDRO','PEDRO','PEDRO','PEDRO','PEDRO','JOAO','JOAO','JOAO','JOAO','JOAO','MARIA','MARIA','MARIA']
print(l1 == l2)
#Sem alterar a lista, pode ser bem util :)
if set(l1) == set(l2):
    print('igual')
else:
    print('diferente')
#Alterando a lista :(
l1 = set(l1)
l2 = set(l2)
print(l1 == l2)




