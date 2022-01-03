perguntas={
    'Pergunta 1':{
        'pergunta': 'Quanto é 2 + 3?',
        'respostas': {'a':'1','b':'5','c':'6'},
        'resposta_certa':'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 2*3?',
        'respostas': {'a':'1','b':'5','c':'6'},
        'resposta_certa':'c',
    },
}

acertou=0
for pergunta_k, dados_v in perguntas.items():
    print(f'{pergunta_k}: {dados_v["pergunta"]}')
    print(f'Respostas: ')
    for resp_k, resp_v in dados_v['respostas'].items():
        print(f'({resp_k}): {resp_v}')

    resposta_usuario = input('A opção correta é:')
    #print(dados_v['resposta_certa'])
    if resposta_usuario.lower() == dados_v['resposta_certa']:
        print('Parabens voce acertou')
        acertou+=1
    else:
        print('Errouu!!')

#Média
qtd_perguntas = len(perguntas)
media = (acertou/qtd_perguntas)*100
print(f'De {qtd_perguntas} perguntas você acertou: {acertou}')
print(f'Sua média de acertos é de {int(media)}%')