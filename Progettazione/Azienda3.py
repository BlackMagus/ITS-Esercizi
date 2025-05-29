class impiegato:
    def __init__(self, nome: str, cognome:str, nascita:str, stipendio:float):
        self.nome = nome
        self.cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio

    def setNome(self, nome:str) -> None:
        if nome:
            self.nome = nome
        else:
            print("Errore! Il nome non può essere una stringa vuota!")

    def setCognome(self, cognome:str) -> None:
        if cognome:
            self.cognome = cognome
        else:
            print("Errore! Il cognome non può essere una stringa vuota!")

    def setNascita(self, nascita:str) -> None:
        if nascita:
            self.nascita = nascita
        else:
            print("Errore! La nascita non può essere una stringa vuota!")

    def setStipendio(self, stipendio:float) -> None:
        if stipendio < 0:
            self.stipendio = stipendio
        else:
            print("Errore! Lo stipendio non può essere un numero negativo!")

class progetto:
    def __init__(self, nome:str, budget:float):
        self.nome = nome
        self.budget = budget

    def setNome(self, nome:str) -> None:
        if nome:
            self.nome = nome
        else:
            print("Errore! Il nome non può essere una stringa vuota!")


        
class dipartimento:
    def __init__(self, nome:str, telefono:str, indirizzo:str):
        self.nome = nome
        self.telefono = telefono
        self.indirizzo = indirizzo

    def setNome(self, nome:str) -> None:
        if nome:
            self.nome = nome
        else:
            print("Errore! Il nome non può essere una stringa vuota!")

    def setTelefono(self, telefono:str) -> None:
        if telefono:
            self.telefono = telefono
        else:
            print("Errore! Il numero di telefono non può essere una stringa vuota!")



    def afferenza(self, data_afferenza:str):
        self.data_afferenza = data_afferenza

    if impiegato:
        print(afferenza)



        