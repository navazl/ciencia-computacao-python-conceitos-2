def sao_multiplicaveis(m1, m2):

    col_m1 = len(m1[0])

    lin_m2 = len(m2)

    if col_m1 == lin_m2:
        return True
    else:
        return False


m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
a = sao_multiplicaveis(m1, m2)
print(a)
