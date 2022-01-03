import re
def limpar_cpf_cnpj(cnpj):
    return re.sub(r'[.-/-]','',cnpj)