from person import Persona

class Dottore(Persona):
    def __init__(self, specialization, parcel):
         
        if isinstance(specialization, str):
            self.specialization:str = specialization
        else:
            self.specialization:str = None
            print("La Specializzazione inserita non è una stringa!")

        if isinstance(parcel, float):
            self.parcel:float = parcel
        else:
            self.parcel:float = None
            print("La parcella inserita non è una valida!")


    def setSpecialization(self, new_specialization):
        if isinstance(new_specialization, str):
            self.specialization = new_specialization
        else:
            new_specialization = None
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, new_parcel):
        if isinstance(new_parcel, float):
            self.parcel = new_parcel
        else:
            new_parcel = None
            print("La parcella inserita non è una valida!")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def validDoctor(self):
        if self.age > 30:
            print("Il nome e il cognome del Dottore sono Validi")
        else:
            print("Il nome e il cognome del Dottore non sono Validi")

    def doctorGreet(self) -> None:
        print(f"{self.greet()} Sono un medico {self.specialization}")
        
        