def verifica_festivita(giorno, mese):
    data = (giorno, mese)
    
    match data:
        case (1, 1):
            return "Capodanno"
        case (14, 2):
            return "San Valentino"
        case (2, 6):
            return "Festa della Repubblica Italiana"
        case (15, 8):
            return "Ferragosto"
        case (31, 10):
            return "Halloween"
        case (25, 12):
            return "Natale"
        case _:
            return "Nessuna festività importante in questa data."

# Input dell'utente
giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))

# Chiamata alla funzione e stampa del risultato
festivita = verifica_festivita(giorno, mese)
print(f"Il {giorno}/{mese} è {festivita}!")
