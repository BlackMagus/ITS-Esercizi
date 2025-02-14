n_tutor = 10
attesa = 0
while attesa < 50:
    studente = (input("Inserire Studente "))
    if n_tutor > 0:
        n_tutor = n_tutor -1
        print("Tutor assegnato con successo")
    else:
        attesa = attesa +1
        print("Studente in attesa")
