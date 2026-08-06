# ESERCIZIO

# Crea una classe Studente con:
# - Attributo di classe scuola = "Liceo Classico"
# - Attributo di istanza nome
# - Metodo di istanza presentati() che stampa "Sono X e frequento Y"
# - Metodo di classe cambia_scuola(cls, nuova_scuola) che modifica la scuola di tutti gli studenti
# Prova creare due studenti e cambia scuola


# Creo la classe Studente con attributo di classe scuola, attributo di istanza nome e metodo presentati()
class Studente:
    scuola = "Liceo Classico"  # Attributo di classe

    def __init__(self, nome):
        self.nome = nome  # Attributo di istanza

    def presentati(self): # Metodo di istanza che stampa la presentazione dello studente
        print(f"Sono {self.nome} e frequento {self.scuola}.")

    @classmethod
    def cambia_scuola(cls, nuova_scuola): # Metodo di classe che modifica l'attributo di classe scuola per tutti gli studenti
        cls.scuola = nuova_scuola

# Svolgimento dell'esercizio:

# Creo due istanze della classe Studente
studente1 = Studente("Luca")
studente2 = Studente("Martin")

# Chiamo il metodo presentati() per entrambi gli studenti
studente1.presentati()  # Output: Sono Luca e frequento Liceo Classico.
studente2.presentati()  # Output: Sono Martin e frequento Liceo Classico.

# Chiamo il metodo di classe cambia_scuola() per modificare la scuola di tutti gli studenti
Studente.cambia_scuola("Liceo Scientifico")

# Chiamo nuovamente il metodo presentati() per entrambi gli studenti
studente1.presentati()  # Output: Sono Luca e frequento Liceo Scientifico.
studente2.presentati()  # Output: Sono Martin e frequento Liceo Scientifico.