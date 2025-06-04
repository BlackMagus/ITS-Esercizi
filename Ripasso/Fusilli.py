x1 = True
y1 = False
z1 = True

def combinazione(x,y,z):
    if x == True and (y or z)==True:
        print("Azione Permessa")

    else:
        print("Azione Negata")

## combinazione(x1,y1,z1)


lista1:list = [24,25,88,90,9,6,7,14]
def moltiplica(lista:list) -> int:
    threshold = 22
    m = 1
    for element in lista:

        if element < threshold:
            m = m * element

        else:
            continue

    return m

## print(moltiplica(lista1))

def sequenza(s):
    if s == "a":
        seq = 2
        for i in range(6):
            print(seq)
            seq = seq + 2

    elif s == "b":
        seq = 1
        for i in range(6):
            print(seq)
            seq = seq + 3

    elif s == "c":
        seq = 30
        for i in range(6):
            print(seq)
            seq = seq -5

    elif s == "d":
        seq = 5
        for i in range(6):
            print(seq)
            seq = seq + 10

## sequenza("a")


def fattoriale(n):
    if n == 1:
        return 1
    else:
        return n * fattoriale(n-1)

print(fattoriale(5))