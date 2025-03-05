def check_lenght(parola:str):
    if len(parola) > 10:
        print(f"La parola {parola} è più lunga di 10 caratteri")
    elif len(parola) < 10:
        print(f"La parola {parola} è più corta di 10 caratteri")
    else:
        print(f"parola è lunga 10 caratteri")

check_lenght("Giovanni")