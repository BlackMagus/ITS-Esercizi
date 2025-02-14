n = int(input("Inserire il numero di coppie da analizare "))
i = 0
p = 0
while i != n:
    x = int(input("Inserire un valore x "))
    y = int(input("Inserire un valore y "))
    if x > 0 and y > 0:
        p = x * y
        print("Il prodotto è ", p)
    else:
        if x < 0 and y < 0:
            print("Errore")
        else:
            p = x + y
            print("La somma è ", p)
    i = i + 1



