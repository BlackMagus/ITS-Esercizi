class persona:
# le informazioni di una persona vengono chiamate attributi e sono: Il nome, il cognome e l'età.
# come li rappresento in python?
    
    def __init__(self, nome:str, cognome:str, età:int):
        self.nome:str = nome
        self.cognome:str = cognome
        self.età:int = età

    def displayData(self) -> None:
        print(f" Nome: {self.nome}\n Cognome: {self.cognome}\n Età: {self.età}")


ab = persona("Alessio", "Basile", 21)
ab.displayData()