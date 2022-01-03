#Producar na documntacao do python mas temos varias funcoes para trabalhar com arquivos w, w+, a, r
#Criado um arquivo
file = open('abc.txt','w+')
file.write('Linha 1 \n')
file.write('Linha 2 \n')
file.write('Linha 3 \n')
#Setando o cursor para o inicio para ler o arquivo
file.seek(0,0)
#Lendo o arquivo
print(file.read())
file.seek(0,0)
#Lendo linha a linha
print(file.readline())
print(file.readline())
file.seek(0,0)
#Lendo e transformando o arquivo em um array, posso fazer um for para percorrer esse cara tambem
print(file.readlines())
file.seek(0,0)
#ou posso fazer o for dirreto no file talmbem da
for line in file:
    print(line, end='')
#Fechando o arquivo
file.close()

#Muitos usam assim para fechar o arquivo
try:
    file = open('abc.txt','w+')
    file.write('Linha try 1 \n')
    file.write('Linha try 2 \n')
    file.seek(0,0)
    print(file.read())
finally:
    file.close()

#Melhor forma de abrir arquivos em python, nesta forma nao precisamos fechar o arquivo
with open('abc.txt', 'w+') as file:
    file.write('Linha with 1 \n')
    file.write('Linha with 2 \n')
    file.write('Linha with 3 \n')
    file.seek(0)
    print(file.read())
#lendo arquivos
with open('abc.txt', 'r') as file:
    print(file.read())

#incrementa dados no arquivo sem alterar o conteudo que já tem
with open('abc.txt', 'a+') as file:
    file.write('DADOS A MAIS')
    file.seek(0)
    print(file.read())

#apagar o arquivo
import os
os.remove('abc.txt')


#Salvando um json em um arquivo
import json
d1 = {
    'Pessoa 1':{
        'nome':'luiz',
        'idade':25,
    },
'Pessoa 2':{
        'nome':'eduardo',
        'idade':44,
    },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)


#Lendo o arquivo json
with open('abc.json', 'r') as file:
    json_f = file.read()
    #COnverter para um dicionario normal
    json_f = json.loads(json_f)
    print(json_f)

#Percorrendo o arquivo
for k,v in json_f.items():
    print(v)