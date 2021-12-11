def imprime_matriz(matriz):
    for i in matriz:
        tamanho = len(i) - 1
        for j, k in enumerate(i):
            if j == tamanho:
                print(f'{k}')
            else:
                print(f'{k} ', end='')


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
