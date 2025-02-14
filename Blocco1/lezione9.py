n = (input("Inserire il nome "))
v = int(input("Inserire la vendita "))
max_nome = n
max = v
min_nome = n
min = v
c = 0
while c != 20:
  new_n = (input("Inserire il prossimo nome "))
  new_v = int(input("Inserire la prossima vendita "))
  if new_v > max:
    max_nome = new_n
    max = new_v
  else:
    if new_v < min:
      min_nome = new_n
      min = new_v
  c = c+1
print (max_nome, max)
print (min_nome, min)
