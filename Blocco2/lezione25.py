punteggio_totale = 0
contatore = 1

while punteggio_totale < 100:
    dado1 = (contatore * 3 + 1) % 6 + 1  
    dado2 = (contatore * 5 + 2) % 6 + 1 
    print(f"Lancio dei dadi: {dado1} e {dado2}")
    
    somma = dado1 + dado2
    
    # Calcolo del punteggio in base alle regole del gioco
    if dado1 % 2 == 0 and dado2 % 2 == 0 and somma > 8:
        punteggio = 100
    elif dado1 == 6 or dado2 == 6 or somma == 7:
        punteggio = 10
    else:
        punteggio = 1  # Aggiungi una condizione che garantisce un incremento anche quando non sono soddisfatte le condizioni precedenti
    
    if punteggio == 100:
        print("Hai vinto! Punteggio 100.")
        punteggio_totale = 100
        break  # Termina il ciclo non appena raggiungi il punteggio 100
    elif punteggio == 0:
        print("Hai perso. Punteggio 0.")
        punteggio_totale = 0
    else:
        punteggio_totale += punteggio
        print(f"Punteggio incrementato di {punteggio}. Punteggio totale: {punteggio_totale}")
    
    contatore += 1

# Risultato finale
if punteggio_totale == 100:
    print("Congratulazioni! Hai vinto il gioco con un punteggio di 100.")
elif punteggio_totale == 0:
    print("Game over. Hai perso con un punteggio di 0.")
