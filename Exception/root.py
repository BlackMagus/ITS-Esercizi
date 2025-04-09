import math

def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "Non puoi fare la radice di un numero negativo"
    

print(safe_sqrt(-4))