n = (input("Inserire il nome "))
print("Hello", n, ", Would you like to learn some Python today?")
famous_person = "Edmond Dantès"
print("Una volta", famous_person, "disse: ", "Ho nel cuore 3 sentimenti con i quali non ci si annoia mai: La Tristezza, l'amore e la riconoscenza.")

names = ["Giuseppe", "Leandro", "Francesca"]
message = {
    "Giuseppe": "Ciao sono Giuseppe, vorrei una panda",
    "Leadro": "Ciao a Tutti! vorrei una moto",
    "Francesca": "Ciao, vorrei un monopattino"
}

for names, message in message.items():
    print(f"{names}: {message}")


Guest =["Francesca", "Alessandro", "Paolo"] 
invite ={
    "Francesca": "Sei invitata alla mia cena, non vedo l'ora di vederti!",
    "Alessandro": "Ciao amico mio! Sei invitato a casa mia domani",
    "Paolo": "Sei invitato alla mia cena domani"
} 
print(f"{Guest}: {invite}")


Listaz = Guest.pop()



print(sorted(names))
names.reverse()
print (names)
len_invitati = len(Guest)
for i in range(len_invitati):
  print (Guest[i])

## 3.10

Finale = ["Filippo", "Giorgio", "Dario"]
print (f"{Finale}")

messaggio = {
    "Filippo": "Buongiorno a tutti!",
    "Giorgio": "Buonasera a tutti!",
    "Dario": "Buonanotte a tutti!"
}

print(sorted(messaggio))


i:int = 1

while i != 11:
    s1 = s1 + i
    i = i + 1

c = 20
while c != 34:
   s2 = s2 + c
   c = c + 1

f = 35

while f != 50:
   s3 = s3 + f
   f = f + 1

print("La somma da 1 a 10 è", s1)
print("La somma da 20 a 35 è", s2)
print("La somma da 35 a 49 è", s3)

