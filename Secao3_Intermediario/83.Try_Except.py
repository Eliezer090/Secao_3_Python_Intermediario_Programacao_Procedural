try:
    print(a)
except NameError as erro:
    print('erro de name')
except Exception as erro:
    print(erro)
else:
    '''Sempre que da sucesso ele passa aqui'''
    print('Executado com sucesso')
finally:
    '''Se ocorre um erro ou nao ele passa aqui, é util para fechar conexoes, limpar variaveis inicializa-las etc.'''
    print('Finally')