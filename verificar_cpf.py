"""
CPF = 168.995.350-09
--------------------------------------------------------
1 * 10 = 10             #     1 * 11 = 11 <--
6 * 9  = 54             #     6 * 10 = 60
8 * 8  = 64             #     8 * 9  = 72
9 * 7  = 63             #     9 * 8  = 72
9 * 6  = 54             #     9 * 7  = 62
5 * 5  = 25             #     5 * 6  = 30
3 * 4  = 12             #     3 * 5  = 15
5 * 3  = 15             #     0 * 3  = 0
0 * 2  = 0              # --> D1 * 2  = 0

y = 11 - ( x % 11 )

        x1 = 297                      x2 = 343
11 - (297 % 11) = 11           11 - (343 % 11) = 9
if y > 9:                      Digito 2 = 9
    D1 = 0
else:
     D1 = y
"""


def verificar_cpf(cpf_informado):
    cpf = cpf_informado[:-2]
    l1 = []
    l2 = []

    for i1, i2 in enumerate(cpf):
        """
        Gera duas lista com valores dos indices e o conteudo. 
        i1 : índice
        i2 : conteudo
        """
        l1.append(int(i1 + 2))
        l2.append(int(i2))
    l1.sort(reverse=True)

    it = 0
    x1 = 0
    for i1 in l1:
        x1 += i1 * l2[it]
        it += 1

    """
    Realiza o calculo para obter o D1:
    y = 11 - ( x % 11 )
    se y > 9, D1 = 0, caso contrario, D1 = y
    """
    y = 11 - (x1 % 11)

    if y > 9:
        D1 = 0
    else:
        D1 = y

    # Criando as listas, so que agora com o valor de D1 e de Y
    # Lista com o índice e com mais um valor na lista dos índices.
    l3 = l1
    l3.append(11)
    l3.sort(reverse=True)

    # Lista com o conteudo e com o valor de D1
    l4 = l2
    l4.append(D1)

    it2 = 0
    x2 = 0

    for i1 in l3:
        x2 += i1 * l4[it2]
        it2 += 1

    """
    Realiza os calculos para obter o valor de D2
     11 - (x2 % 11) = D2

    """

    D2 = 11 - (x2 % 11)
    DF = str(D1) + str(D2)
    cpf_valido = cpf[:9] + DF

    if cpf_informado == cpf_valido:
        print(f'\nCPF: {cpf_informado}')
        print('Status: VALIDO')
    else:
        print(f'\nCPF: {cpf_informado}')
        print(f'CPF GERADO: {cpf_valido}')
        print('Status: Invalido')