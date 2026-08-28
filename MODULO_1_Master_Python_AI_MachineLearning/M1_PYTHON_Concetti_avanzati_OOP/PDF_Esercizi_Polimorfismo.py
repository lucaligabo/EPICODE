# ESERCIZIO

# Crea una classe base Forma con metodo area().
# Crea due classi derivate:
# Rettangolo -> area = base * altezza
# Cerchio -> area = π * r²
# Crea una lista di forme e stampa l'area di ciascuna usando lo stesso metodo area

# Svolgimento

# Importo math per π
from math import pi

# Creo classe Forma
class Forma:
    def area(self):
        pass

# Creo classe Rettangolo 
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    def area(self):                     # Ridefinisco il metodo area
        return self.base * self.altezza

# Creo classe Cerchio
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
    def area(self):                     # Ridefinisco il metodo area
        return pi * self.raggio ** 2

# Creo lista di forme
forme = [
    Rettangolo(base=10, altezza=5),  # riporto il nome attributo per chiarezza, si può fare senza ma rispettando ordine
    Cerchio(raggio=5.2),
    Rettangolo(base=7, altezza=15),
    Cerchio(raggio=8)
]

# Creo ciclo per stampare la lista numerata con ciascun output di area 
for i, forma in enumerate(forme, start=1):
    print(f"Forma {i}: {type(forma).__name__}, area = {forma.area():.2f}")
