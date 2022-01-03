"""
Somar o valor total do carrinho utilizando listCompreheison
"""

carrinho = [
    ('prd 1',30),
    ('prd 2',20),
    ('prd 3',50)
]

tot=[]
tot = sum([valor for nome, valor in carrinho])
print(tot)









