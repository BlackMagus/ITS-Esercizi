a = int(input("Vuoi inserire A "))
b = int(input("Vuoi inserire B "))
if a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            s = 0
            i = a
            while i < b:
                s = s + i
                i = i + 1
            print("La somma è ", s)
        else:
            print("A e B devono essere interi!")
    else:
        print("A e B devono essere positivi!")
else:
    print("A deve essere minore di B!")
