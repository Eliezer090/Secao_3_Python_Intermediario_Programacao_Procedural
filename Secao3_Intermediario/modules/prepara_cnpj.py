from Intermediario.Secao3_Intermediario.modules.limpar_cpf_cnpj import limpar_cpf_cnpj


def preparaCnpj(cnpj):
    cnpj = limpar_cpf_cnpj(cnpj)
    return cnpj[0:12]