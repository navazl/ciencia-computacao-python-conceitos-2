def ordenada(lista):
    fim = len(lista)

    lista_inicial = []

    for elemento in lista:
        lista_inicial.append(elemento)

    for i in range(fim - 1):
        posicao_do_minimo = i

        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    if lista_inicial == lista:
        return True
    else:
        return False
