class Alieno:
    
    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    
    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota!")

    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    
    def speak(self) ->None:
        print("jifejfiedjkfiefkjedcfkl")


    def __str__(self) -> str:
        return f"Alieno proveniente dalla galassia: {self.getGalaxy()}"