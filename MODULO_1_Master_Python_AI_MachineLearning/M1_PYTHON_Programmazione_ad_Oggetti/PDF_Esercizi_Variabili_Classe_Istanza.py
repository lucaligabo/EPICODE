# ESERCIZIO

# Crea una classe Automobile con:
# - Variabile di classe ruote = 4
# - Variabile di instanza modello
# Crea due automobili con modelli diversi e stampa il numero di ruote e i modelli

# Creo classe Automobile
class Automobile:
    ruote = 4  # Variabile di classe (condivisa da tutte le istanze)

    def __init__(self, modello):
        self.modello = modello   # Variabile di istanza (specifica per ciascun oggetto)

# Creazione di due automobili con modelli diversi
auto1 = Automobile("Fiat 500")
auto2 = Automobile("Tesla Model 3")

# Stampa del numero di ruote e dei modelli
print(f"Auto 1: Modello = {auto1.modello}, Ruote = {auto1.ruote}")
print(f"Auto 2: Modello = {auto2.modello}, Ruote = {auto2.ruote}")
        