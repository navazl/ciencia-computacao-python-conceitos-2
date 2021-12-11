def mais_curto(lista_nomes):
    mais_curto = lista_nomes[0]
    for n in lista_nomes:
        nome = n.strip()
        if len(nome) < len(mais_curto):
            mais_curto = nome
        else:
            pass
    print(mais_curto.capitalize())


lista_de_nomes = ['   ana   ', '   jeferson   ', '  junin ', '  michelle ']
mais_curto(lista_de_nomes)
