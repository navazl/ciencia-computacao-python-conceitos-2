def busca(lista, elemento):
    for c, i in enumerate(lista):
        print(f'\n{i}\n')
        if i == elemento:
            return c
    return False
