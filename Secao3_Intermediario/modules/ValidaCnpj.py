def valida_cnpj(cnpj_Original, cnpj_Gerado):
    if valida_Sequencia(cnpj_Original) and cnpj_Gerado == cnpj_Original:
        return True

    return False

def valida_Sequencia(cnpj_Original):
    sequencia = cnpj_Original[0] * len(cnpj_Original)
    if sequencia != cnpj_Original and len(cnpj_Original) == 14:
        return True

    return False

