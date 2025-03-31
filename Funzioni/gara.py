import random

def Tartaruga(c1):
    i = random.randint(1,10)
    if i >= 1 and i <= 5:
        c1 = c1 + 3  #passo veloce

    elif i >= 6 and i <= 7:
        c1 = c1 - 6  #Scivolata
        if c1 < 0:
            c1 = 1

    elif i >= 8 and i <= 10:
        c1 = c1 + 1  #Passo Lento

    if c1 > 70:
        c1 = 70
    return c1


def Lepre(c2):
    i = random.randint(1,10)
    if i >= 1 and i <= 2:
        c2 = c2 + 0  #Riposo

    elif i >= 3 and i <= 4:
        c2 = c2 + 9 #Grande Balzo

    elif i >= 5:
        c2 = c2 - 12  #Grande Scivolata
        if c2 < 0:
            c2 = 1

    elif i >= 6 and i <= 8:
        c2 = c2 + 1 #Piccolo Balzo

    elif i >= 9 and i <= 10:
        c2 = c2 - 2 #Piccola Scivolata
        if c2 < 0:
            c2 = 1

    if c2 > 70:
        c2 = 70
    return c2
     
def Posizione(c1,c2):
    if c1 == c2:
        # Se tartaruga e lepre sono nella stessa posizione
        print('OUCH!!!')
    print(percorsoT)
    print(percorsoL)

    return True



percorsoT = ["_"] * 71
percorsoL = ["_"] * 71
tick = 0
print("BANG !!!!! AND THEY'RE OFF !!!!!")
tartaruga = 1
lepre = 1
while percorsoT[-1] != "T" and percorsoL[-1] != "L":
     # Muovi la tartaruga
    tartaruga = Tartaruga(tartaruga)
    percorsoT = ["_"] * 71 
    percorsoT[tartaruga] = "T"
    
    # Muovi la lepre
    lepre = Lepre(lepre)
    percorsoL = ["_"] * 71  
    percorsoL[lepre] = "L"

    Posizione(tartaruga, lepre)
    
    tick = tick + 1
    print(f"Passato {tick} tick")

if percorsoT[-1] == "T":
    print("TORTOISE WINS! || VAY!!!")
elif percorsoL[-1] == "L":
    print("HARE WINS || YUCH!!!")
else:
    print("IT'S A TIE.")

