# ESERCIZIO

# Crea una classe Frazione che rappresenti una frazione con numeratore e denominatore.
# Implementa i seguenti operatori:
# - + (somma tra frazioni)
# - == (uguaglianza tra frazioni, sempificando i valori)
# - __str__ per stampare la frazione come "3/4"


# Svolgimento

class Frazione:
    def __init__(self, numeratore, denominatore):
        # Se il denominatore è zero, non facciamo nulla
        # perché vogliamo evitare errori e non usare raise
        if denominatore != 0:
            self.numeratore = numeratore
            self.denominatore = denominatore
        else:
            # Se il denominatore è zero, lasciamo i valori di default
            self.numeratore = 0
            self.denominatore = 1

    def semplifica(self):
        # Calcolo il massimo comune divisore (MCD)
        mcd = self._mcd(abs(self.numeratore), abs(self.denominatore))

        # Divido numeratore e denominatore per il MCD
        self.numeratore //= mcd
        self.denominatore //= mcd

        # Se il denominatore è negativo, porto il segno al numeratore
        if self.denominatore < 0:
            self.numeratore = -self.numeratore
            self.denominatore = -self.denominatore

    def _mcd(self, a, b):
        # Algoritmo di Euclide per trovare il MCD
        while b:
            a, b = b, a % b
        return a

    def __add__(self, altra):
        # Somma fra due frazioni:
        # a/b + c/d = (a*d + c*b) / (b*d)
        nuovo_num = self.numeratore * altra.denominatore + altra.numeratore * self.denominatore
        nuovo_den = self.denominatore * altra.denominatore

        # Creo un nuovo oggetto con il risultato
        risultato = Frazione(nuovo_num, nuovo_den)

        # Semplifico il risultato
        risultato.semplifica()
        return risultato

    def __eq__(self, altra):
        # Confronto due frazioni
        # Se l'oggetto passato non è una frazione, ritorno False
        if not isinstance(altra, Frazione):
            return False

        # Confronto il valore delle frazioni
        return self.numeratore / self.denominatore == altra.numeratore / altra.denominatore

    def __str__(self):
        # Mostro la frazione come "numeratore/denominatore"
        return f"{self.numeratore}/{self.denominatore}"



f1 = Frazione(3, 4)
f2 = Frazione(1, 2)

risultato = f1 + f2
print(risultato)      # stampa 5/4

print(f1 == f2)       # stampa False
print(Frazione(2, 4)) # stampa 2/4