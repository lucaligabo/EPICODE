# ESERCIZIO

# Crea un file libri.csv e con colonne: titolo, autore, anno.
# Scrivi una classe GestoreLibri che legga il file e stampi i titoli.
# Aggiungi un metodo che stampi i libri di un certo autore

# Svolgimento

import csv
import os

# Creo classe GestoreLibri
class GestoreLibri:
    def __init__(self, nome_file):
        # Salvo il nome del file
        self.nome_file = nome_file

    def aggiungi_libro(self, titolo, autore, anno):
        # Controllo se il file non esiste oppure è vuoto
        file_vuoto = (
            not os.path.exists(self.nome_file)
            or os.path.getsize(self.nome_file) == 0
        )

        # Apro il file in modalità append
        with open(self.nome_file, "a", newline="", encoding="utf-8") as file:
            scrittore = csv.DictWriter(
                file,
                fieldnames=["titolo", "autore", "anno"]
            )

            # Scrivo l'intestazione se il file è nuovo o vuoto
            if file_vuoto:
                scrittore.writeheader()

            # Aggiungo il libro al file
            scrittore.writerow({
                "titolo": titolo,
                "autore": autore,
                "anno": anno
            })

    def stampa_titoli(self):
        # Apro il file in modalità lettura
        with open(self.nome_file, "r", newline="", encoding="utf-8") as file:
            lettore = csv.DictReader(file)
            libri = list(lettore)

            # Controllo se il file non contiene libri
            if not libri:
                print("File vuoto.")
                return

            # Mostro all'utente i titoli dei libri
            print("\nTitoli dei libri:")
            for libro in libri:
                print(libro["titolo"])

    def libri_di_autore(self, autore_cercato):
        # Apro il file in modalità lettura
        with open(self.nome_file, "r", newline="", encoding="utf-8") as file:
            lettore = csv.DictReader(file)
            trovato = False

            print(f"\nLibri di {autore_cercato}:")

            # Cerco i libri dell'autore indicato
            for libro in lettore:
                if libro["autore"].lower() == autore_cercato.lower():
                    print(f"- {libro['titolo']} ({libro['anno']})")
                    trovato = True

            # Comunico all'utente se non ho trovato libri
            if not trovato:
                print("Nessun libro trovato.")

    def cancella(self):
        # Apro il file in modalità scrittura per svuotarlo
        with open(self.nome_file, "w", encoding="utf-8"):
            pass


# Creo un oggetto GestoreLibri
gestore = GestoreLibri("libri.csv")

# Chiedo all'utente di inserire almeno un libro
while True:
    titolo = input("Inserisci il titolo del libro: ").strip()
    autore = input("Inserisci l'autore: ").strip()
    anno = input("Inserisci l'anno: ").strip()

    # Controllo che tutti i dati siano stati inseriti
    if titolo and autore and anno:
        gestore.aggiungi_libro(titolo, autore, anno)
        break

    print("Devi inserire titolo, autore e anno.")

# Chiedo all'utente se vuole inserire altri libri
while True:
    risposta = input("\nVuoi inserire un altro libro? (s/n): ").lower()

    if risposta == "n":
        break

    if risposta == "s":
        titolo = input("Inserisci il titolo del libro: ").strip()
        autore = input("Inserisci l'autore: ").strip()
        anno = input("Inserisci l'anno: ").strip()

        # Controllo che tutti i dati siano stati inseriti
        if titolo and autore and anno:
            gestore.aggiungi_libro(titolo, autore, anno)
        else:
            print("Libro non aggiunto: devi compilare tutti i campi.")
    else:
        print("Rispondi inserendo 's' oppure 'n'.")

# Mostro all'utente tutti i titoli presenti nel file
gestore.stampa_titoli()

# Chiedo all'utente quale autore vuole cercare
autore_cercato = input("\nInserisci un autore da cercare: ").strip()
gestore.libri_di_autore(autore_cercato)

# Chiedo all'utente se vuole svuotare il file
risposta = input("\nVuoi svuotare il file? (s/n): ").lower()

if risposta == "s":
    gestore.cancella()
    print("Il file è stato svuotato.")
else:
    print("Il file non è stato modificato.")