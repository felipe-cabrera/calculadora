def fatorial(numero):
    fat = 1
    mult = 2

    while mult <= numero:
        fat = fat * mult
        mult += 1

    return fat
