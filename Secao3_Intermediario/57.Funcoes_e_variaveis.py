var = 'valor'

def func1():
    print(var)

def func2():
    var = 'valor2'
    print(var)

func1()
func2()
#Uma variavel criada fora e usada detro da função se tentar atribuir o valor a ela o valor global nao é alterado
print(var)

print('--alterando valor---')
#Caso quiser alterar o valor da variavel de dentro da variavel por algum motivo, mas nao é recomendado
def func3():
    global var
    var = 'outro valor'
    print(var)
print(var)
func3()
print(var)

print('------Alterar-----')
var = 'valor'

def func4():
    #print(var) #se tentar assim da ruim pq a global nao é reconhecida se tentar alterar o valor
    var = 222
    print(var)

func4()




