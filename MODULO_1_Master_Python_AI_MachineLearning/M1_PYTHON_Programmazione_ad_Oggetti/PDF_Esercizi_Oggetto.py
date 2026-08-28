# ESERCIZIO

# Scrivi una classe Studente con attributi nome e corso, e un metodo presentati() che stampa
# una frase di presentazione.


# Creare la classe Studente con gli attributi nome e corso
class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

# Defizione del metodo presentati() che stampa una frase di presentazione
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e sto studiando {self.corso}.")


# Svolgimento dell'esercizio: Creare un'istanza della classe Studente e chiamare il metodo presentati()

studente1 = Studente("Luca", "Informatica")
studente1.presentati()