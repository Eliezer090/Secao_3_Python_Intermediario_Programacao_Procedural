from dados import produtos,pessoas,lista

nova_lista = map(lambda x:x*2,lista)
print(lista)
print(list(nova_lista))

print("Dicionarios:")

for produto in produtos:
    print(produto)
#Adicionar 5% ao valor dos produtos, mas sem alterar a extrutura original
print('Aumenta em 5% o valor dos produtos:')
def aumnetaPreco(p):
    p['preco'] = round(p['preco']*1.05,2)
    return p

precos = map(aumnetaPreco,produtos)
for produto in precos:
    print(produto)

#Pega Nome das pessoas
print("Pessoas: ")
for pessoa in pessoas:
    print(pessoa)

nomes = map(lambda p:p['nome'],pessoas)
for nome in nomes:
    print(nome)

#Cria novo elemento dentro do docionario
print('Novo Elemento: ')
def nova_idade(p):
    #AUmenta em 20% a idade das pessoas
    p['nova_idade'] = round(p['idade']*1.20)
    return p

novo_dic = map(nova_idade,pessoas)
for pessoa in novo_dic:
    print(pessoa)