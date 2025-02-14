c = 0
s = 0
m = 0
scelta = (input("Vuoi inserire il voto? "))
while scelta == "si":
  v = int(input("Inserire voto "))
  scelta = (input("Vuoi inserire un altro voto? "))
  if v > 0:
    c = c + 1
    s = s + v
  else:
    print("Impossibile inserire questo voto")
if scelta == "no":
  m = s / c
  print("La media è ", m)
else:
  print("Scelta non valida")

