n = (input("Inserire il nome "))
print("Hello", n, ", Would you like to learn some Python today?")
famous_person = "Edmond Dantès"
print("Una volta", famous_person, "disse: ", "Ho nel cuore 3 sentimenti con i quali non ci si annoia mai: La Tristezza, l'amore e la riconoscenza.")

names = ["Giuseppe", "Leandro", "Francesca"]
message = {
    "Giuseppe": "Ciao sono Giuseppe, per gli amici Peppe!",
    "Leadro": "Ciao a Tutti!",
    "Francesca": "Ciao Peppe!"
}

for names, message in message.items():
    print(f"{names}: {message}")

