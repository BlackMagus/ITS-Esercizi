dizionario:dict = { "Banana": 8, "Mele": 12, "Pane": 56, "Melone" : 52}

def prezzi(dizionario1:dict)-> dict:
    dizionario2:dict = {}
    for element in dizionario1:
        key,value = element[0], element[1]

        if value < 50:
            dizionario2[key]= value + (value * 1.10)
            
        else:
            continue
        
    return dizionario2

print(prezzi(dizionario))