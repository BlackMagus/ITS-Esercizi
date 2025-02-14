x = int(input("Inserire il valore di x "))
i = 0
s = 0
if x < 0:
    print("Errore")
else:
    while i != 10:
      n = int(input("Inserire un valore "))
      if x % 2 == 0:
         if n > x / 2:
            s = s + n
      else:
         if n < x:
           s = s + n
      i = i + 1
