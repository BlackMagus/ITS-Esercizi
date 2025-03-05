def read_numbers(n:list):
    for a in n:
        if a > 5:
            print(f"{a} è più grande di 5")
        elif a == 5:
            print(f"{a} è uguale a 5")
        else:
            print(f"{a} è minore di 5")

j = [4, 8, 12, 16, 89]

read_numbers(j)