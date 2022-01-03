
from vendas.calc_precos import aumento,reducao

preco = 49.90
preco_com_aumento = aumento(preco,15)
print(preco_com_aumento)

preco_com_reducao = reducao(preco,15)
print(preco_com_reducao)
