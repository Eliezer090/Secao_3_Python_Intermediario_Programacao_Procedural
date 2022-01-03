from Intermediario.Secao3_Intermediario.vendas.formata.preco import real


def aumento(valor, porcentagem):
    return real(valor + (valor * (porcentagem / 100)))


def reducao(valor, porcentagem):
    return real(valor - (valor * (porcentagem / 100)))

if __name__ == '__main__':
    print(aumento(49.90, 15))
