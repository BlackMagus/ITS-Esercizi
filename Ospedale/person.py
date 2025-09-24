class Persona:

    def __init__(self, first_name:str, last_name:str,):

        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            self._first_name = None
            print("Il nome inserito non è una stringa!")

        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            self._last_name = None
            print("Il cognome inserito non è una stringa!")
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            self.age = None
        elif isinstance(first_name, str) and isinstance(last_name, str):
            self.age = 0
        
    def setName(self, new_name)  -> None:
        if isinstance(new_name, str):
            self._first_name = new_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self, new_lastName) -> None:
        if isinstance(new_lastName, str):
            self._last_name = new_lastName
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, new_age)  -> None:
        if isinstance(new_age, int):
            self.age = new_age
        else:
            print("Il numero inserito non è intero!")

    def getName(self):
        return self._first_name
    
    def getLastName(self):
        return self._last_name
    
    def getAge(self):
        return self.age
    
    def greet(self) -> None:
        print(f"Ciao, sono {self._first_name} {self._last_name}! Ho {self.age} anni!")

p = Persona("12", "Rossi")
p.setAge(32)
p.greet()