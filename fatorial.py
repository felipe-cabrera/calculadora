def fatorial(numero):
    # 4 * 3 * 2 * 1
    # 1 * 2 * 3 * 4
    
    fat = 1 
    mult = 2
    
    while mult <= numero:
        fat = fat * mult
        mult = mult + 1
    
    return(fat)
