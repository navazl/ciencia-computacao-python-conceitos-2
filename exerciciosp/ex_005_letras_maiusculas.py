def maiusculas(frase):
    frase_final = ''
    for letra in frase:

        if letra == letra.upper() and letra.isalpha() == True:
            frase_final = frase_final + letra
    return frase_final


if __name__ == "__main__":
    print(maiusculas('Programamos em Python 3'))
