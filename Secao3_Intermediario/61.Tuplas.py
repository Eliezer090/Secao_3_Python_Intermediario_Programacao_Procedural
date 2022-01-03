#Tuplas sai imutaveis
t1=(1,2,3,5,'a')

print(t1)
#Interagir
for v in t1:
    print(v)

#fatiar
print(t1[2:])
#tuplas tambem
t2=1,2,3,4
print(t2)
t3=1,
print(t3,type(t3))

#repetir tupla
t4=(1,2,3,4)*3
print(t4)

#Editar
t5=(1,2,3,4) #isso é imutavel
t5=list(t5) #lista é mutavel
t5[2]=300
print(t5,type(t5))
#voltar a ser tupla
t5=tuple(t5)
print(t5,type(t5))












