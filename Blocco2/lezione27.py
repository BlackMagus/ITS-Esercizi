i = int(input("Quanti numeri ci sono? "))
sp = 0
sd = 0
sm = 0
m = 0
v = i
while i != 0:
    n = int(input("Inserire il numero "))
    if n % 2 == 0:
        if n > m:
            sp = sp + n
    else:
        if n < m:
            sd = sd + n
    sm = sm + n
    m = sm / v
    print("La media è: ", m)
    i = i - 1
print("La somma dei numeri pari è: ", sp)
print("La somma dei numeri Dispari è: ", sd)
if sp > sd:
    print("La somma dei numeri pari è maggiore della somma dei numeri dispari")
else:
    print("La somma dei numeri dispari è maggiore della somma dei numeri pari")

