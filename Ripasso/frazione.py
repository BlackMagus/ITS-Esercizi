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
        print(f"{self.numeratore} / {self.denominatore}")


    def mcd(self):
        x = self.numeratore
        y = self.denominatore
        if x < y:
            while y != 0:
                x, y = y, x % y
            return x
        else:
            while x != 0:
                y, x = x, y % x
            return y
        
        
n = Frazione(12,17)
print(n.mcd())