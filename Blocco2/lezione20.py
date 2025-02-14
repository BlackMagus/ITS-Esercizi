n = int(input("Inserire n "))
if n > 0:
    c = 0
    i = 0
    while i != 10:
        x = int(input("Inserire il numero "))
        if x % n == 0:
          c = c + 1
        i = i + 1
    print("i numeri divisibili per n sono: ", c)
else:
   print(" n deve essere positivo!")
        