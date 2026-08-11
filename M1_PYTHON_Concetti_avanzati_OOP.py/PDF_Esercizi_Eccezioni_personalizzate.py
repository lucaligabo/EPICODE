# ESERCIZIO

# Crea una classe Studente con attributo età.
# - Se l età è negativa, solleva EtàNonValidaError.

# Cra una classe Magazzino con metodo rimuovi_prodotto(nome, quantità)
# - Se non ci sono abbastanza pezzi, solleva ProdottoEsuaritoError.

# (Facoltativo) Organizza le tue eccezioni sotto un classe base ErroreScuola o ErroreMagazzino


# Svolgimento

# - Creo le classe base per le eccezioni
class ErroreScuola(Exception):
    pass

class EtàNonValidaError(ErroreScuola):
    pass

class ErroreMagazzino(Exception):
    pass

class ErroreProdottoEsauritoError(ErroreMagazzino):
    pass


# Creo classe Studente con attributo età e controllo per "raise"
class Studente:
    def __init__(self, età):
        if età < 0:
            raise EtàNonValidaError("L'età non può essere negativa")
        self.età = età

# Creo classe Magazzino con metodo rimiuovi_prodotto(), solleva errore in caso di mancanza pezzi
class Magazzino:
    def __init__(self, prodotti):
        self.prodotto = prodotti

    def rimuovi_prodotto(self,articolo , quantità):
        disponibilità = self.prodotto.get(articolo, 0)

        if quantità > disponibilità:
            raise ErroreProdottoEsauritoError(f"Il proddoto {articolo} è esurito.")
        self.prodotto -= quantità


# Esempio Studenti

try:
    studente = Studente(-25)
except EtàNonValidaError as errore:
    print("errore")




# Esempio prodotti magazzino

magazzino = Magazzino({"Quaderni": 20, "Pennarelli": 50})

try:
    magazzino.rimuovi_prodotto("Quaderni", 25)
except ErroreProdottoEsauritoError as errore:
    print(errore)
