#ESERCIZIO

# Crea una classe Studente che chieda all'utente nome ed età e abbia un metedo presentati()
# - Aggiungi a uno studente un metedo __str__ che restituisca una stringa leggibile

# Crea una classe Diario che salvi su file un messaggio passato dall'utente.
# (Facoltativo) Aggiungi un metedo che legga dal file e stampi i messeggi

# Svolgimento

# Creo classe studente
class Studente:
    def __init__(self):
        self.nome = input("Inserisci il tuo nome: ")
        self.eta = int(input("Inserisci la tua età: "))
# Metodo presentati
    def presentati(self):
        print(f"Ciao! Mi chiamo {self.nome}, e ho {self.eta} anni.")
# Mertedo __str__ personalizzato
    def __str__(self):
        return f"Studente: {self.nome}, Età: {self.eta}"


# Creo Classe diaro
class Diario:
    def __init__(self, nome_file="diario.txt"):
        self.nome_file = nome_file

    def salva_messaggio(self, messaggio):
        with open(self.nome_file, "a", encoding="utf-8") as file:
            file.write(messaggio + "\n")

    def leggi_messaggi(self):
        with open(self.nome_file, "r", encoding="utf-8") as file:
            print(file.read())


studente = Studente()
studente.presentati()
print(studente)

diario = Diario()
messaggio = input("Inserisci un messaggio: ")
diario.salva_messaggio(messaggio)

# Facoltativo: legge e stampa tutti i messaggi
diario.leggi_messaggi()