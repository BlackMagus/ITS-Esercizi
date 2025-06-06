class ContactManager:

    def __init__(self, contacts:dict[str,list[str]]):
        self.contacts = contacts


    def create_contact(self, name:str, phone_numbers:list[str]):
        if name in self.contacts:
            raise ValueError("Errore: il contatto esiste già")
        else:
            self.contacts[name] = phone_numbers
            return {name: phone_numbers}
    

    def add_phone_number(self,contact_name:str, phone_number:str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste")
        elif phone_number in self.contacts:
            raise ValueError("Errore: il numero di telefono esiste già")
        else:
            self.contacts[contact_name].append(phone_number)
            return {contact_name: self.contacts[contact_name]}
        
    def remove_phone_number(self, contact_name:str, phone_number:str):
        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        elif phone_number not in self.contacts[contact_name]:
            raise ValueError ("Errore: il numero di telefono non esiste")
        else:
            self.contacts[contact_name].remove(phone_number)
            return {contact_name: self.contacts[contact_name]}
        

    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str):
        if contact_name not in self.contacts:
            raise ValueError("il contatto non esiste")
        if old_phone_number not in  self.contacts[contact_name]:
            raise ValueError("il numero non è presente")
        
        index: int = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}


