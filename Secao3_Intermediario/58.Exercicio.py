"""
Criar Funções que recebam funções por parametros e seus parametros
Em geral é para utilziar os *args e **kwargs
"""

def func2():
    return '2'

def func3(numero):
    return 1+numero

def func4(*args):
    return args[0]+args[1]

def func5(**kwargs):
    return kwargs.get('valor1')+kwargs.get('valor2')

def func1(funcao, *args,**kwargs):
    return funcao(*args,**kwargs)

print(func1(func2))
print(func1(func3, 2))
print(func1(func4, 2, 3))
print(func1(func5, valor1=3, valor2=3))