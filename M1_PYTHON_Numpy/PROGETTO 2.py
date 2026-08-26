# Programma completo per la gestione semplice di pazienti, medici e analisi
# Implementa: variabili, classi OOP, uso di NumPy e integrazione in un main

import numpy as np

# -------------------------
# PARTE 1 - Variabili e tipi di dati (esempi semplici)
# -------------------------

# Definizione di almeno 3 pazienti come variabili separate (esempio)
nome1 = "Mario"
cognome1 = "Rossi"
codice_fiscale1 = "RSSMRA45A01H501X"
eta1 = 45
peso1 = 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

nome2 = "Lucia"
cognome2 = "Bianchi"
codice_fiscale2 = "BNCLCU32B41F205Y"
eta2 = 32
peso2 = 60.0
analisi2 = ["glicemia", "colesterolo", "TSH"]

nome3 = "Paolo"
cognome3 = "Verdi"
codice_fiscale3 = "VRDPLA29C22G345Z"
eta3 = 29
peso3 = 82.0
analisi3 = ["emocromo", "glicemia", "ferritina"]

# -------------------------
# PARTE 2 - Classi e OOP
# -------------------------

class Analisi:
    # Classe per rappresentare una singola analisi con tipo e risultato numerico
    def __init__(self, tipo: str, risultato: float):
        self.tipo = tipo  # tipo di analisi (es. "glicemia")
        self.risultato = risultato  # valore numerico della misura

    def valuta(self) -> str:
        # Metodo che valuta se il risultato è nella norma usando criteri semplificati
        t = self.tipo.lower()
        v = self.risultato
        if t == "glicemia":
            # glicemia a digiuno (mg/dL) - intervallo di riferimento semplificato
            if 70 <= v <= 110:
                return "normale"
            elif v < 70:
                return "basso"
            else:
                return "alto"
        elif t == "colesterolo":
            # colesterolo totale (mg/dL)
            if v < 200:
                return "normale"
            elif v < 240:
                return "borderline"
            else:
                return "alto"
        elif t in ("emocromo", "emoglobina", "hb"):
            # emoglobina (g/dL) range semplificato (unisex per esempio)
            if 12 <= v <= 17:
                return "normale"
            elif v < 12:
                return "basso"
            else:
                return "alto"
        elif t == "ferritina":
            # ferritina (ng/mL) range molto semplificato
            if 20 <= v <= 200:
                return "normale"
            elif v < 20:
                return "basso"
            else:
                return "alto"
        elif t == "tsh":
            # TSH (µIU/mL) range semplificato
            if 0.4 <= v <= 4.0:
                return "normale"
            elif v < 0.4:
                return "basso"
            else:
                return "alto"
        else:
            # Per tipi non riconosciuti, non è possibile dare una valutazione precisa
            return "valutazione non disponibile"

    def __str__(self):
        # Rappresentazione testuale dell'analisi con valutazione
        return f"{self.tipo}: {self.risultato} ({self.valuta()})"


class Paziente:
    # Classe per rappresentare un paziente con attributi richiesti
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, eta: int, peso: float,
                 analisi_effettuate: list = None, risultati_analisi: np.ndarray = None):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        # lista dei nomi delle analisi eseguite (stringhe)
        self.analisi_effettuate = analisi_effettuate if analisi_effettuate is not None else []
        # array NumPy con i risultati numerici (allineati con analisi_effettuate)
        self.risultati_analisi = risultati_analisi if risultati_analisi is not None else np.array([])

    def scheda_personale(self) -> str:
        # Restituisce una stringa con i dati principali del paziente
        return (f"Scheda Paziente: {self.nome} {self.cognome} - CF: {self.codice_fiscale} - "
                f"Età: {self.eta} - Peso: {self.peso} kg")

    def aggiungi_analisi(self, tipo: str, risultato: float):
        # Aggiunge un'analisi aggiornando la lista e l'array NumPy dei risultati
        self.analisi_effettuate.append(tipo)
        if self.risultati_analisi.size == 0:
            self.risultati_analisi = np.array([risultato], dtype=float)
        else:
            self.risultati_analisi = np.append(self.risultati_analisi, float(risultato))

    def statistiche_analisi(self) -> dict:
        # Calcola media, minimo, massimo e deviazione standard usando NumPy
        if self.risultati_analisi.size == 0:
            return {"media": None, "min": None, "max": None, "std": None}
        media = float(np.mean(self.risultati_analisi))
        minimo = float(np.min(self.risultati_analisi))
        massimo = float(np.max(self.risultati_analisi))
        std = float(np.std(self.risultati_analisi, ddof=0))  # ddof=0 opzionale: valore predefinito, esplicitato per chiarezza del calcolo della dev. standard
        return {"media": media, "min": minimo, "max": massimo, "std": std}

    def stampa_analisi_dettaglio(self):
        # Stampa ogni analisi con il valore e la valutazione
        for tipo, valore in zip(self.analisi_effettuate, self.risultati_analisi):
            a = Analisi(tipo, valore)
            print(f"  - {a}")  # utilizza __str__ di Analisi

    def __str__(self):
        return f"{self.nome} {self.cognome} (CF: {self.codice_fiscale})"


class Medico:
    # Classe per rappresentare un medico
    def __init__(self, nome: str, cognome: str, specializzazione: str):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente: Paziente):
        # Stampa quale medico sta visitando quale paziente
        print(f"Il Dr./Dr.ssa {self.nome} {self.cognome} ({self.specializzazione}) sta visitando {paziente.nome} {paziente.cognome}.")

    def __str__(self):
        return f"Dott. {self.nome} {self.cognome} - {self.specializzazione}"


# -------------------------
# PARTE 3 - Uso di NumPy (esempio con 10 valori)
# -------------------------
# Esempio: raccolta di 10 valori per un particolare esame (es. glicemia)
valori_esame_10 = np.array([85, 92, 110, 76, 99, 120, 88, 101, 95, 82], dtype=float)

# Calcoli con NumPy
media_10 = np.mean(valori_esame_10)
massimo_10 = np.max(valori_esame_10)
minimo_10 = np.min(valori_esame_10)
std_10 = np.std(valori_esame_10, ddof=0)  # ddof=0 opzionale: valore predefinito, esplicitato per chiarezza del calcolo della dev. standard

# -------------------------
# PARTE 4 & 5 - Integrazione OOP + NumPy e Applicazione completa (main)
# -------------------------

def main():
    # Creazione di almeno 3 medici
    medici = [
        Medico("Anna", "Moretti", "Cardiologia"),
        Medico("Giovanni", "Ricci", "Endocrinologia"),
        Medico("Sara", "Fabbri", "Medicina Generale")
    ]

    # Creazione di almeno 5 pazienti, ciascuno con almeno 3 risultati di analisi
    p1 = Paziente("Marco", "Neri", "NRIMRC40D12L219A", 40, 75.0)
    p1.aggiungi_analisi("glicemia", 95)
    p1.aggiungi_analisi("colesterolo", 185)
    p1.aggiungi_analisi("emocromo", 14.2)

    p2 = Paziente("Elena", "Gallo", "GLLENN28E08M563B", 28, 62.5)
    p2.aggiungi_analisi("glicemia", 105)
    p2.aggiungi_analisi("colesterolo", 205)
    p2.aggiungi_analisi("tsh", 2.1)

    p3 = Paziente("Roberto", "Sala", "SLARBT55F20P404C", 55, 90.0)
    p3.aggiungi_analisi("glicemia", 130)
    p3.aggiungi_analisi("colesterolo", 250)
    p3.aggiungi_analisi("ferritina", 18)

    p4 = Paziente("Laura", "Ferrari", "FRRLRA33H66C987D", 33, 68.0)
    p4.aggiungi_analisi("glicemia", 82)
    p4.aggiungi_analisi("colesterolo", 170)
    p4.aggiungi_analisi("emocromo", 13.5)

    p5 = Paziente("Alessio", "Conti", "CNTLSS45K12E111E", 45, 80.0)
    p5.aggiungi_analisi("glicemia", 90)
    p5.aggiungi_analisi("colesterolo", 195)
    p5.aggiungi_analisi("ferritina", 60)

    pazienti = [p1, p2, p3, p4, p5]

    # Stampare la scheda di ogni paziente e i dettagli delle analisi
    print("=== SCHEDE PAZIENTI ===")
    for paz in pazienti:
        print(paz.scheda_personale())
        paz.stampa_analisi_dettaglio()
        stats = paz.statistiche_analisi()
        # Stampa delle statistiche calcolate con NumPy (controllo None per sicurezza)
        if stats["media"] is None:
            print("  Nessun risultato disponibile per questo paziente.")
        else:
            print(f"  Statistiche (media/min/max/std): "
                  f"{stats['media']:.2f} / {stats['min']:.2f} / {stats['max']:.2f} / {stats['std']:.2f}")
        print("-" * 60)

    # Mostrare quale medico visita quale paziente (associazione round-robin come esempio)
    print("\n=== VISITE MEDICI ===")
    for i, paz in enumerate(pazienti):
        medico = medici[i % len(medici)]
        medico.visita_paziente(paz)

    # Stampare i risultati dell'esempio con 10 valori
    print("\n=== ESEMPIO NUMPY: 10 VALORI DI UN'ANALISI ===")
    print("Valori:", valori_esame_10)
    print(f"Media: {media_10:.2f}, Min: {minimo_10:.2f}, Max: {massimo_10:.2f}, DevStd: {std_10:.2f}")

# Eseguire main se il file è eseguito come script
if __name__ == "__main__":
    main()

