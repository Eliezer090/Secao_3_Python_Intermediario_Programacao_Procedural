
'''
Faca uma lista de tarefas com as opcoes:
    Adicionar tarefas
    listar tarefas
    Opcao de desfazer a ultima acao
    Opcao de refazer a ultima acao
'''
array = []
arrayDesfeito = []
while True:
    print('1-Adicionar tarefa')
    print('2-Listar tarefas')
    print('3-Desfazer')
    print('4-Refazer')
    entrada = input('Digite a acao que deseja: ')
    try:
        if entrada == '1':
            valor = input('Digite a tarefa a ser adicionada: ')
            array.append(valor)
        elif entrada == '2':
            print(array)
        elif entrada == '3':
            arrayDesfeito.append(array[-1])
            array.pop(-1)
        elif entrada == '4':
            array.append(arrayDesfeito[-1])
            arrayDesfeito.pop(-1)
        elif entrada.upper() == 'Q':
            break
        else:
            print(f'Valor {entrada} nao é reconhecido')
    except IndexError as err:
        if entrada == '3':
            print(f'nao há indices para serem removidos')
        elif entrada == '4':
            print('Nao há indice para ser adicionado')
    except Exception as erro:
        print(f'Valor digitado inválido: {erro}')