##  Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
##  Make a method called describe_user() that prints a summary of the user’s information.
##  Make another method called greet_user() that prints a personalized greeting to the user.
##  Create several instances representing different users, and call both methods for each user.

class user:

    def __init__(self, first_name:str, last_name:str, email:str, birthday:str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday

    def describe_user(self) -> None:
        print(f" Il nome è {self.first_name}\n Il cognome è {self.last_name}\n l'email è {self.email}\n ed è nato il {self.birthday}")


    def greet_user(self) -> None:
        print(f" {self.first_name} benvenuto nel nostro sito!!")

gigi = user("Gigi", "Calli", "ggigione@gmail.com", "27 ottobre")

gigi.describe_user()
gigi.greet_user()        