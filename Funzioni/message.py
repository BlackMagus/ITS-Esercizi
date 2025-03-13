def show_messages(myList:list):
    print(myList)



def send_messages(myList:list, myList2:list):
    while myList:
        myList2.append(myList.pop(0))

    print("Messaggi rimasti sono: ", myList)
    print("I messaggi inviati sono: ", myList2)




n:list = ["Ciao", "Buonasera", "Buongiorno", "Salve"]

show_messages(n)

sent_message:list = []

send_messages(n, sent_message)