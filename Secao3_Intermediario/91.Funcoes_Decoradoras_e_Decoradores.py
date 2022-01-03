'''Funcoes decoradoras servem para adicionar recursos a funcoes
já existentesm, ou seja, temos uma funcao Outra e queremos adicionar algo a
mais a esta funcao, com isso decoramos a funcao outra com a @master, podendo
incrementar coisas a mais em uma funcao.'''

def master(funcao):
    def slave(*args, **kwargs):
        print('decorada')
        funcao(*args, **kwargs)
    return slave
#A segunda forma de decorar funcao é assim
@master
def falaoi():
    print('oi_funcao')

#sem o args e kwargs da erro essa funcao
@master
def outra(msg):
    print(msg)
#Assim é uma forma se docora uma funcao
#falaoi = master(falaoi)
#falaoi()
outra("alguma coisa")


#Funcao que conta o tempo que a funcao demora para executar com decorador
from time import time
from time import sleep
def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado= funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) *1000
        print(f'A funcao: {funcao.__name__} levou {tempo:.2f}ms')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()