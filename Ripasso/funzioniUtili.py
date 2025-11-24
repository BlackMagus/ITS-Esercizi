# def conta(lista:list[str]):
#    parole = []
#    i = 0
#    diz2 = {}
#    for element in lista:
#        element.lower()
#        parole.extend(element.split())
#        if element in parole:
#            i = i + 1
#        diz1 = {
#            element : i
#        }
#       diz2.update(diz1)

def ordina(lista: list[int]):
    m = len(lista)
    for i in range(m):  
        for j in range(m - 1 - i):  
            if lista[j] < lista[j + 1]:  
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    print(lista)

n = [1, 2, 3, 4, 56, 78, 22]
ordina(n)  
