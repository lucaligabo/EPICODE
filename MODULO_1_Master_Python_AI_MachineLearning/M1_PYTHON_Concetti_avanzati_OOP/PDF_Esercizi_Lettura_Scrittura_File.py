# ESERCIZIO

# Crea un classe Appunti che salvi in un file ogni riga scritta dall'utente.
# - Aggiungi un metodo mostra() che stampi il contenuto del file.
# - Estendi la classe con un metodo cancella() che svuoti il File

# Svolgimento

# Creo classe Appunti
class Appunti:
    def __init__(self, nome_file="appunti.txt"):
        # Salvo il nome del file da utilizzare
        self.nome_file = nome_file

    # Metodo per scrivere su file
    def scrivi(self, riga):
        # Apro il file in modolità "append", per non cancellare eventuali appunti già presenti
        with open(self.nome_file, "a", encoding="utf-8") as file:
            file.write(riga + "\n")

    # Metedo per leggere il file
    def mostra(self):
        # Apro il file in modolità lettura
        with open(self.nome_file, "r", encoding="utf-8") as file:
            # Stampo il contenuto del file a video
            print(file.read())

    # Metedo per svuotare il file
    def cancella(self):
        # Apro il file in modolità scrittura per svuotarlo
        with open(self.nome_file, "w", encoding="utf-8") as file:
            pass



appunti = Appunti()

# Acquisisco e salvo righe scritte dall'utente
while True:
    riga = input("Scrivi una riga (Premi invio per terminare): ")

    if riga == "":
        break

    appunti.scrivi(riga)

# Mostro il contenuto del file
print("\nContenuto degli appunti:")
appunti.mostra()

# Chiedo all'utente se vuole svuotare il file
risposta = input("\nVuoi svuotare il file? (s/n): ").lower()

if risposta == "s":
    appunti.cancella()
    print("Il file è stato svuotato.")
else:
    print("Il file non è stato modificato.")
