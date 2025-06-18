class Frazione:
    def __init__(self, numeratore:float, denominatore:float):
        self.numeratore = numeratore
        self.denominatore = denominatore


    def setter(self) -> None:
        if not self.numeratore.is_integer() or self.denominatore.is_integer():
            self.numeratore = 13
            self.denominatore = 5
        else:
            raise ValueError("Il numero è già intero")
        
        if self.denominatore == 0:
            self.denominatore = 5

    def value(self):

        n = self.numeratore / self.denominatore

        r = round(n, 3)
        return r
    
    def __str__(self)-> None:
        
        return (f"{self.numeratore} / {self.denominatore}")
        


def mcd(x,y):
    if x < y:
        while y != 0:
            x, y = y, x % y
        return x
    else:
        while x != 0:
            y, x = x, y % x
        return y
    
        
def semplifica(l:list[Frazione]):

    lista_irriducibili = []

    for frazione in l:
        num = frazione.numeratore
        den = frazione.denominatore
        divisore = mcd(num, den)

        num_sempl = num // divisore
        den_sempl = den // divisore

        frazione_irriducibile = Frazione(num_sempl, den_sempl)
        lista_irriducibili.append(frazione_irriducibile)

    return lista_irriducibili


m = Frazione(12,24)
r = Frazione(34,89)
n:list[Frazione] = [m,r]

print(semplifica(n))