import random

def calcola_carichi(matrice):
    m = len(matrice)
    
    somme_righe = [sum(riga) for riga in matrice]
    
    somme_colonne = [sum(matrice[r][c] for r in range(m)) for c in range(m)]
    
    carichi = [[somme_righe[r] - somme_colonne[c] for c in range(m)] for r in range(m)]
    
    return carichi


# Esempio
matrice = [
    [1, 2, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 2, 0],
    [2, 0, 0, 0]
]

carichi = calcola_carichi(matrice)

for r in range(len(matrice)):
    for c in range(len(matrice)):
        print(f"k({r},{c}) = {carichi[r][c]}")




def genera(dim):
    matrice = []
    for _ in range(dim):
        primo = random.randint(0, 13)
        riga = [primo]
        while len(riga) < dim:
            n = random.randint(0, 13)
            if n != primo:
                riga.append(n)
        
        matrice.append(riga)
    
    return matrice
