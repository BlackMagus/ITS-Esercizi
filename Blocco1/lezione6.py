n = int(input("Inserire il numero "))
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n*fattoriale(n-1)
print ("Il fattoriale è: ", fattoriale(n))