def menor_nome(nomes):
    menor_nome = nomes[0].strip()
    for nome in nomes:
        nome = nome.strip()

        if len(nome) < len(menor_nome):
            menor_nome = nome
    return menor_nome.capitalize()
