n = int(input("Inserire il numero "))
if n < 2:
    print("Il numero non è primo")
else:
    Div:int = 2
    while Div < n:
        if n % Div == 0:
            print ("Il numero non è primo")
        Div = Div + 1
print ("Il numero è primo")

