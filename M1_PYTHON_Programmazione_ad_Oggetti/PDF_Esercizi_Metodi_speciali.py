# ESERCIZIO

# Crea una classe Libro con attributi titolo, autore.
# - Nel __init__(), inizializza i valori
# - Nel __str__(), restituisca una frase tipo:"Titolo: X, Autore: Y"

# Svolgimento

# Creo classe Libro con attributi titolo, autore
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}"

# Creo un istanza Libro e la stampo

libro = Libro("Dracula", "Bram Stoker")
print(libro)
