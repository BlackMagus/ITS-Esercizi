Max = int(input("Inserisci il massimo "))
CONT:int = 1
while CONT < 4:
      n = float(input("Inserisci il numero "))
      if n > Max:
        Max = n
      CONT = CONT + 1
print(Max)
