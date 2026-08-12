# Progetto 1  

#=====================================
# Gestione di una biblioteca digitale
#=====================================

# - Parte 1: variabili e tipi di dati
# - Parte 2: strutture dati (lista, dizionario, set)
# - Parte 3: classi e OOP (Libro, Utente, Prestito)
# - Parte 4: funzionalità (presta_libro, gestione prestiti e stampa risultati)

# -----------------------
# Parte 1 - Variabili e tipi di dati
# 1) Titolo di un libro (stringa)
# 2) Numero di copie disponibili (intero)
# 3) Prezzo medio di un libro (float)
# 4) Stato disponibile/non disponibile (booleano)

titolo_esempio = "Il Signore degli Anelli"   # stringa (esempio)
copie_esempio = 5                            # intero (esempio)
prezzo_medio = 18.50                         # float (esempio)
disponibile = copie_esempio > 0              # booleano (True se ci sono copie)

# -----------------------
# Parte 2 - Strutture dati

# 1) Lista con almeno 5 titoli di libri
titoli_libri = [
    "Il Signore degli Anelli",
    "1984",
    "Orgoglio e pregiudizio",
    "Il nome della rosa",
    "Harry Potter e la pietra filosofale",
]

# 2) Dizionario che mappa titolo -> numero di copie disponibili
copie_per_libro = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Orgoglio e pregiudizio": 2,
    "Il nome della rosa": 4,
    "Harry Potter e la pietra filosofale": 6,
}

# 3) Insieme (set) con utenti registrati
utenti_registrati = {"Luca", "Anna", "Marco"}


# ------------------------
# Eccezioni personalizzate - aggiunta personale
# ------------------------
# 

# Usate per la Parte 4: gestione degli errori con try/except/raise
class CopieNonDisponibiliError(Exception):
    # Errore sollevato quando un libro non ha copie disponibili.
    pass

class DurataPrestitoNonValidaError(ValueError):
    # Errore sollevato quando la durata del prestito non è valida.
    pass


# -----------------------
# Parte 3 - Classi e OOP

# 1) Classe Libro con attributi titolo, autore, anno, copie_disponibili
class Libro:
    # Rappresenta un libro presente nella biblioteca.
    def __init__(self, titolo: str, autore: str, anno: int, copie_disponibili: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self) -> str:
        # Metodo info(): restituisce una stringa descrittiva del libro.
        stato = "disponibile" if self.copie_disponibili > 0 else "non è disponibile"
        return (
            f"{self.titolo} di {self.autore} ({self.anno}) - "
            f"copie disponibili: {self.copie_disponibili} ({stato})"
        )

# 2) Classe Utente con attributi nome, età, id_utente
class Utente:
    # Rappresenta un utente registrato.
    def __init__(self, nome: str, eta: int, id_utente: int):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self) -> None:
        # Metodo scheda(): stampa i dati dell'utente.
        print(f"Utente: {self.nome} | Età: {self.eta} | ID: {self.id_utente}")

# 3) Classe Prestito che collega Utente e Libro e contiene giorni
class Prestito:
    # Collega un utente a un libro per un certo numero di giorni.
    def __init__(self, utente: Utente, libro: Libro, giorni: int):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self) -> None:
        # Metodo dettagli(): stampa tutte le informazioni sul prestito.
        print(
            f"{self.utente.nome} (ID {self.utente.id_utente}) ha preso "
            f'"{self.libro.titolo}" per {self.giorni} giorni.'
        )


# -----------------------
# Parte 4 - Funzionalità

# Funzione presta_libro(utente, libro, giorni):
# - Verifica se il libro ha almeno 1 copia (altrimenti raise CopieNonDisponibiliError)
# - Verifica che giorni > 0 (altrimenti raise DurataPrestitoNonValidaError)
# - Se ok: decrementa copie_disponibili e crea il Prestito

def presta_libro(utente: Utente, libro: Libro, giorni: int) -> Prestito:
    # Registra e ritorna un oggetto Prestito oppure solleva un'eccezione.
    if giorni <= 0:
        # Solleva un'eccezione specifica per durata non valida
        raise DurataPrestitoNonValidaError("La durata del prestito deve essere maggiore di zero.")

    if libro.copie_disponibili < 1:
        # Solleva un'eccezione specifica per copie non disponibili
        raise CopieNonDisponibiliError(f'Il libro "{libro.titolo}" non ha copie disponibili.')

    # Riduce il numero di copie e crea il prestito
    libro.copie_disponibili -= 1
    prestito = Prestito(utente, libro, giorni)
    print(f'Prestito registrato: "{libro.titolo}" assegnato a {utente.nome}.')
    return prestito


# -----------------------
# Main: demo e simulazioni (inclusi try/except per mostrare la gestione degli errori)

def main() -> None:
    # Stampa variabili di esempio (Parte 1)
    print("=== Variabili di esempio ===")
    print(f"Titolo: {titolo_esempio}")
    print(f"Copie: {copie_esempio}")
    print(f"Prezzo medio: {prezzo_medio:.2f} euro")
    print(f"Disponibile: {disponibile}")

    # Mostra strutture dati (Parte 2)
    print("\n=== Strutture dati ===")
    print("Lista titoli:", titoli_libri)
    print("Copie per libro:", copie_per_libro)
    print("Utenti registrati:", sorted(utenti_registrati))

    # Crea alcuni oggetti Libro e Utente (Parte 3)
    libri = [
        Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 5),
        Libro("1984", "George Orwell", 1949, 3),
        Libro("Orgoglio e pregiudizio", "Jane Austen", 1813, 2),
    ]
    utenti = [
        Utente("Luca", 25, 1),
        Utente("Anna", 30, 2),
        Utente("Marco", 22, 3),
    ]

    # Stampa schede utenti (Metodo scheda() della classe Utente)
    print("\n=== Schede utenti ===")
    for utente in utenti:
        utente.scheda()

    # Stampa catalogo iniziale (Metodo info() della classe Libro)
    print("\n=== Catalogo iniziale ===")
    for libro in libri:
        print(libro.info())

    # PRESTITI: prova a registrare 3 prestiti diversi (Parte 4)
    # Qui si usa try/except per catturare le eccezioni definite sopra senza fermare il programma.
    prestiti_effettuati = []
    richieste_prestito = [
        (utenti[0], libri[0], 14),  # Luca prende "Il Signore..."
        (utenti[1], libri[1], 7),   # Anna prende "1984"
        (utenti[2], libri[2], 21),  # Marco prende "Orgoglio e pregiudizio"
    ]

    print("\n=== Registrazione prestiti ===")
    for utente, libro, giorni in richieste_prestito:
        try:
            prestito = presta_libro(utente, libro, giorni)
        except CopieNonDisponibiliError as errore:
            # Gestione specifica per copie esaurite
            print(f"Errore copie: {errore}")
        except DurataPrestitoNonValidaError as errore:
            # Gestione specifica per durata non valida
            print(f"Errore durata: {errore}")
        else:
            # Se non ci sono eccezioni, salva il prestito nella lista
            prestiti_effettuati.append(prestito)

    # Esempi espliciti di gestione degli errori (mostrati separatamente)
    print("\n=== Esempi di gestione degli errori ===")

    # Esempio 1: tentativo di prestito di un libro senza copie (solleva CopieNonDisponibiliError)
    libro_esaurito = Libro("Il nome della rosa", "Umberto Eco", 1980, 0)
    try:
        presta_libro(utenti[0], libro_esaurito, 14)
    except CopieNonDisponibiliError as errore:
        print(f"Errore copie gestito correttamente: {errore}")

    # Esempio 2: tentativo di prestito con durata non valida (solleva DurataPrestitoNonValidaError)
    try:
        presta_libro(utenti[1], libri[0], 0)
    except DurataPrestitoNonValidaError as errore:
        print(f"Errore durata gestito correttamente: {errore}")

    # Stampa elenco aggiornato delle copie disponibili (richiesto nella consegna)
    print("\n=== Copie disponibili aggiornate ===")
    for libro in libri:
        print(f"{libro.titolo}: {libro.copie_disponibili}")

    # Stampa i dettagli di ogni prestito effettuato (richiesto nella consegna)
    print("\n=== Dettagli prestiti ===")
    for prestito in prestiti_effettuati:
        prestito.dettagli()

# Esecuzione quando il file viene avviato direttamente
if __name__ == "__main__":
    main()