pari:int = 0
dispari:int = 0
c = 0
while c != 10:
    n = int(input("Inserire il numero "))
    if n % 2 == 0:
        pari = pari+1
    else:
        dispari= dispari+1
    c = c+1
print(pari)
print(dispari)