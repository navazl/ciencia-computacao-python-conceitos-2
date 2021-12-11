def dimensoes(matriz):
    return f"{len(matriz)}x{len(matriz[0])}"


def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        lin = len(m1)
        col = len(m1[0])
        nova_matriz = []
        for i in range(lin):
            linha = []
            for j in range(col):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            nova_matriz.append(linha)
        return nova_matriz
    else:
        return False


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
a = soma_matrizes(m1, m2)
print(a)
