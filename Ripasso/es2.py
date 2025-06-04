lista:list = [1,2,3,4,5,-7,-8]

def converti(lista_numeri:list) -> dict:
    dizionario1:dict = {"positivi": [], "negativi": []}

    for element in lista_numeri:
        if element >= 0:
            dizionario1["positivi"].append(element)

        else:
            dizionario1["negativi"].append(element)

    return dizionario1

print (converti(lista))
