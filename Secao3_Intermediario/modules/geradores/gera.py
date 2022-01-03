import random
def gerador(cnpj):
    primeiro = gera_digitos(cnpj, 1)
    cnpj += str(primeiro)
    segundo = gera_digitos(cnpj, 2)
    cnpj += str(segundo)
    return cnpj


def gera_digitos(cnpj, digito):
    soma = 0
    regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        regressivos = regressivos[1:]
    elif digito == 2:
        regressivos = regressivos
    else:
        regressivos = []
    for p, n in enumerate(regressivos):
        soma += int(cnpj[p]) * n

    gerado = 11 - (soma % 11)
    return str(gerado) if gerado <= 9 else 0

def gera_cnpj():
    primeiro = random.randint(0, 9)
    segundo = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    cnpj = f'{primeiro}{segundo}{segundo_bloco}{terceiro_bloco}{quarto_bloco}'
    return gerador(str(cnpj))
