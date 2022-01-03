#*args e **kwargs

def func(*args):
    print(args)
    print(args[0])

func([1,2,3,4,5])

#Convertendo o args para lista
def func2(*args):
    lista = list(args)
    lista[0]=20
    print(lista)
    #posso percorrer o args tambem
    for v in args:
        print(v)

func2(1,2,3,4,5)

#mandando a lista desempacotada
lista=[1,2,3,4,5]
print(lista)
print(*lista)
#com separador que eu quiser
print(*lista,sep='-')
#Com mais um valor indo junto
print(*lista,'6',sep='-')

"""
args e kwargs
args = para receber qualquer parametro cuidar na ordem pois terão suas posições dentro da tupla
kwargs = Parametros nomeados nao importa a posição deles pois terao seus nomes
kwargs a principio sao melhores.
"""
def func3(*args,**kwargs):
    print(args)
    print(kwargs)
    #usando o get se nao tiver ele retorna none, usando o [] ele da erro se não tiver
    print(kwargs['nome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    print(idade)
    if idade is not None:
        print(idade)

func3('parametro1',nome='Eliezer', sobrenome='Schwartz')
func3('parametro2',nome='joao', sobrenome='paulo',idade=11)






