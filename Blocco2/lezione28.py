
giorni_settimana = ["Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato", "Domenica"]
temperature = []

for i in range(7):
    temp = float(input(f"\n inserisci la temperatura per {giorni_settimana[i]}: "))
    temperature.append(temp)

    media = sum(temperature) / len(temperature)

    if all(10 <= temp <= 30 for temp in temperature):
        stato = "Temperatura Variabile"
    else:
        stato = "Allerta Temperatura"

    max_temp = max(temperature)
    min_temp = min(temperature)
    giorno_max = temperature.index(max_temp) + 1
    giorno_min = temperature.index(min_temp) + 1

    print(f"\n Temperatura media: {media:.2f}°C")
    print(stato)
    print(f"Giorno con temperatura più alta: {max_temp} {giorni_settimana[giorno_max - 1]}")
    print(f"Giorno con temperatura più bassa: {min_temp} {giorni_settimana[giorno_min - 1]}")