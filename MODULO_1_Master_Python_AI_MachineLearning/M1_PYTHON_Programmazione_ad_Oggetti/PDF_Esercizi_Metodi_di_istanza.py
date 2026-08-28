# ESERCIZIO

# Crea una classe Studente con attributi nome e età.
# Istanzia due studenti diversi e stampane i dati.
# - Aggiungi alla classe studente un metodo presentati() che stampi un messagio con nome e età dello studente.
# - Prova ad aggiungere un attributo "al volo" a uno studente, ad esempio "corso" e stampalo.

# Creo la classe Studente con attributi nome e età
class Studente:
    def __init__(self, nome, eta):
        self.nome = nome  # Attributo di istanza nome
        self.eta = eta    # Attributo di istanza età

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

# Svolgimento dell'esercizio: Creare due istanze della classe Studente e chiamare il metodo presentati()
studente1 = Studente("Luca", 38)
studente2 = Studente("Martin", 25)

studente1.presentati()
studente2.presentati()

# Aggiungo un attributo "al volo" a uno studente, ad esempio "corso"
studente1.corso = "Informatica"  # Aggiungo l'attributo corso all'istanza studente1
print(f"{studente1.nome} sta studiando {studente1.corso}.")
