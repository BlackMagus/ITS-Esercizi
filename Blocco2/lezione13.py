num_NS = int(input("Inserire Veicoli di Nord-Sud "))
num_EO = int(input("Inserire Veicoli di Est-Ovest "))
s = int(input("Inserire il valore soglia "))
tp = int(input("Inserire tempo di priorità "))
if num_NS > s:
    if num_EO:
        tempo_NS = 50
        tempo_EO = 50
    else:
        tempo_NS = tp
        tempo_EO = 100 - tp
else:
    if num_EO > s:
        tempo_NS = 100 - tp
        tempo_EO = tp
    else:
        tot_veicoli = num_NS + num_EO
        tempo_NS = num_NS / tot_veicoli*100
        tempo_EO = 100 - tempo_NS
print ("il tempo di attesa della coda nord-sud è", tempo_NS, "il tempo di attesa della cosa est-ovest", tempo_EO)