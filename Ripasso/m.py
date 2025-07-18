def calculateCharges(ora):
    t = 0.00
    if ora > 3: 
        if ora == 24:
          t = 10.00
        else:
            r = ora
            r = r - 3
            while r != 0:
                t = t + 2.50
                r = r - 1

            if r < 0:
                t = t + 0.50

    else:
        t = 2.00

    return t


cars:list[float] = [1.5, 4.0, 5.5, 24.0]
totale = 0
print(f"{"ar" :<10} {"Hours" :<10} {"Charges" :<10}")
for i in totale(len(cars)):
    T = calculateCharges(cars[i])
    print(f"{i + 1 : <10} {cars[i] : <10} {T : <.2f}")
    totale = totale + T

print(f"{"Total" :<10} {sum(cars):<10} {totale :<.2f}")

