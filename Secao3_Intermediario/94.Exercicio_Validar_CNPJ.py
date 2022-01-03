#Validar CNPJS
from Intermediario.Secao3_Intermediario.modules.ValidaCnpj import valida_cnpj, valida_Sequencia
from Intermediario.Secao3_Intermediario.modules.geradores.gera import gerador
from Intermediario.Secao3_Intermediario.modules.limpar_cpf_cnpj import limpar_cpf_cnpj
from modules.prepara_cnpj import preparaCnpj
while True:
    cnpj_original = input('Digite o CNPJ: ')
    try:
        if cnpj_original == 'Q':
            break
        if cnpj_original != '' and valida_Sequencia(limpar_cpf_cnpj(cnpj_original)) :
            cnpj = preparaCnpj(cnpj_original)

            if valida_cnpj(limpar_cpf_cnpj(cnpj_original),gerador(cnpj)):
                print('CNPJ Valido')
            else:
                print('CNPJ Invalido')
        else:
            print('CNPJ Invalido')
    except:
        print('Algo deu errado, favor revise o CNPJ!')






