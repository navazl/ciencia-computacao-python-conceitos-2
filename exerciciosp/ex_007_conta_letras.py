def conta_letras(frase, contar="vogais"):
    numero_total = 0
    frase = frase.lower()
    if contar == "vogais":
        for c in frase:
            if c in "aeiou":
                numero_total += 1
    elif contar == "consoantes":
        for c in frase:
            if c in "bcdfghjklmnpqrstvwxyz":
                numero_total += 1
    print(numero_total)


conta_letras('programamos em python', 'consoantes')
