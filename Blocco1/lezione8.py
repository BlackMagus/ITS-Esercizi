soglia = int(input("Inserire la soglia "))
c = 0
while c != 7:
  n = int(input("Inserire il numero "))
  if n > soglia:
    print("Questo numero supera la soglia: ", n)
  c = c+1
