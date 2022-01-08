from verificar_cpf import verificar_cpf
from gerar_cpf import gerar_cpf
print('1 - VERIFICAR CPF'
      '\n2 - GERAR CPF')
op = int(input('OPÇÃO: '))

if op == 1:
    cpf_informado = input('Informe um CPF: ')
    verificar_cpf(cpf_informado)

elif op == 2:
    gerar_cpf()