def gestione_corso():
    corso = (input("Inserire il nome del corso "))
    tot_posti = 100
    posti_occ = 0

    while posti_occ < tot_posti:
        print("/Menu")
        print("- Iscrivi uno studente")
        print("- Annulla iscrizione")
        print("- Visualizza stato corso")
        print("- Elimina il corso e crea un nuovo corso")
        print("- Esci")

        scelta = (input("Scegli una delle opzioni proposte "))

        if scelta == "Iscrivi uno studente":
            if posti_occ < tot_posti:
                posti_occ = posti_occ + 1
                print("Studente iscritto con successo")
            else:
                print("Il corso è al completo, impossibile effettuare l'iscrizione")

        elif scelta == "Annulla iscrizione":
            if posti_occ > 0:
                posti_occ = posti_occ - 1
            else:
                print("Non ci sono Studenti iscritti")

        elif scelta == "Visualizza stato corso":
            posti_liberi = tot_posti - posti_occ
            print(f"Posti occupati: {posti_occ}")
            print(f"Posti liberi: {posti_liberi}")

        elif scelta == "Elimina il corso":
            print(f"Il corso {corso} è stato eliminato")
            return gestione_corso()
        
        elif scelta == "Esci":
            print("Chiusura del programma")
            break

        else:
            print("Scelta non valida. Riprova")

gestione_corso()

