n = int(input("Inserire un numero "))
i = 0
s = 0
if  n > 0:
    while i <= n:
        s = s + i**2
        i = i + 1
else:
    print("errore")
if s != 0:
  print("La somma dei quadrati è ", s)




