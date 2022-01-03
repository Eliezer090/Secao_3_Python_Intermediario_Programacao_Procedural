from dados import produtos,pessoas,lista
#Filtrando valores > 5
nova_lista = filter(lambda x: x>5,lista)
print(list(nova_lista))

#Filtrando um docionario
print("FilterDoc:")

nova_lista = filter(lambda p: p['preco']>50,produtos)
for produto in nova_lista:
    print(produto)

#Caso precisar fazer algo mais complexo pode fazer uma função
print('Função:')
def filtra(produto):
    if produto['preco'] >50:
        return True

    return False

nova_lista = filter(filtra,produtos)
for produto in nova_lista:
    print(produto)

#QUal pessoa é maior de idade
print('Maior de idade:')
def filtra(pessoa):
    if pessoa['idade'] >=18:
        return True

    return False

nova_lista = filter(filtra,pessoas)
for produto in nova_lista:
    print(produto)
