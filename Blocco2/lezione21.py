età = int(input("Qual è la tua età? "))
if età >= 18 and età <= 65:
    print("Puoi partecipare all'attività")
else:
    if età < 18:
        print("Non puoi partecipare all'attività perchè nopn hai raggiunto l'età minima")
    else:
        print("Non puoi partecipare all'attività perchè hai superato l'età massima")

