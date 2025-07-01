class Documento:

    def __init__(self,testo:str):
        self.testo = testo

    def getText(self):
        return self.testo
    
    def islnText(self, parola):
        if parola in self.testo:
            return True
        else:
            print("Questa parola non è presente nel testo")
            return False
        
    
class Email(Documento):

    def __init__(self, mittente:str, destinatario:str, titolo:str):
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getText(self)-> None:
        print(f"Da: {self.mittente} \n Titolo: {self.titolo} \n Messaggio: {self.testo}")

    def writeToFile(self, path):
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.getText())
        except IOError as e:
            print(f"Errore durante la scrittura nel file: {e}")

class File(Documento):

    def __init__(self, percorso):
        self.percorso = percorso

    def leggiTestoDaFile(self):
        with open(f"Document.txt in {self.percorso}", 'r', encoding='utf-8') as file:
            self.testo = file.read()


    def getText(self)-> None:
        print(f"Percorso: {self.percorso} \n Contenuto: {self.testo}")
        
        
