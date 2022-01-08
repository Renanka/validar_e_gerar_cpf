from random import randint
from verificar_cpf import verificar_cpf


def gerar_cpf():
    cpf_gerado = randint(100000000, 999999999)
    cpf = str(cpf_gerado)
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

    # Criando as listas, so que agora com o valor de D1 e com o novo índice
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
    verificar_cpf(cpf_valido)