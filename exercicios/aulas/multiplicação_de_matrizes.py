import cria_matriz


def imprime_matriz(matriz):
    for i in matriz:
        tamanho = len(i) - 1
        for j, k in enumerate(i):
            if j == tamanho:
                print(f'{k}')
            else:
                print(f'{k} ', end='')


def multiplicar_matrizes(A, B):
    num_lin_A, num_col_A = len(A), len(A[0])
    num_lin_B, num_col_B = len(B), len(B[0])
    assert num_col_A == num_lin_B
    C = []
    for lin in range(num_lin_A):
        # Começando uma nova linha
        C.append([])
        for col in range(num_col_B):
            # Adicionando uma nova coluna na linha
            C[lin].append(0)
            for k in range(num_col_A):
                C[lin][col] += A[lin][k] * B[k][col]
    return C


m1 = [[1, 0, 2], [0, 3, 1], [1, 4, -1]]
m2 = [[0, 0, 3], [1, 2, 5], [-1, 0, 1]]
a = multiplicar_matrizes(m1, m2)
print('\n\n\n\n\n')
imprime_matriz(a)
