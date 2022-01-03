"""
Quebrar a string de 10 em 10 caracteres que fica com os numero de 0 a 9 em cada bloco,
    e depois juntar ela mas separado por .
"""
string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
n=10
l1 = [string[i: i+n] for i in range(0,len(string),n)]
l2 = '.'.join(l1)
print(l1)
print(l2)









