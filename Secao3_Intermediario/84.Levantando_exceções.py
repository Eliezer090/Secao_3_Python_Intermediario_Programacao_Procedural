def divide(n1,n2):
    try:
        return n1/n2
    except Exception as erro:
        #Por exemplo aqui loga o erro em um banco nao sei e abaixo repassa ela para quem chamou
        print('Log:',erro)
        #Repassa a exeção para quem chamou
        raise

try:
    print(divide(1/0))
except Exception as erro:
    print(erro)
