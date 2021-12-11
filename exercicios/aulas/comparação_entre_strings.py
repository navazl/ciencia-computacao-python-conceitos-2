def menor_string(array_de_strings):
    atual_menor = ''
    atual_ord = 0
    for string in array_de_strings:
        if ord(string[0]) > atual_ord:
            atual_ord = ord(string[0])
            atual_menor = string
