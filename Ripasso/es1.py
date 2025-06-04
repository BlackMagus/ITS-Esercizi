lista_tuple:list[tuple] = [(1,"A"),(2,"B"),(3,"C")]

def converti(lista:list[tuple]) -> dict:
    dizionario1:dict[any,any] = {}
    for element in lista:
        key,value = element[0], element[1]
        if  key in dizionario1:
            dizionario1[key]+= value

        else:
            dizionario1[key]= value

    return dizionario1
