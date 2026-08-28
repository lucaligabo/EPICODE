#scrivere un programma che analizza un testo e calcola varie statistiche.

#Contare il numero totale di parole.

#Calcolare la frequenza di ogni parola.

#Estrarre le parole uniche usando un set.

#Mostrare le 5 parole più frequenti.

#Calcolare la lunghezza media delle parole.


def pulisci_testo(testo):
    simboli = ",.;:!?()"
    for s in simboli:
        testo = testo.replace(s, "")
    return testo.lower()

def conta_parole(testo):
    parole = testo.split()
    return len(parole)

def frequenza_parole(testo):
    parole = testo.split()
    freq = {}
    for p in parole:
        freq[p] = freq.get(p, 0) + 1
    return freq

def parole_uniche(freq):
    return set(freq.keys())

def top_n_parole(freq, n=5):
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]

def lunghezza_media(freq):
    tot_caratteri = sum(len(p) * occ for p, occ in freq.items())
    tot_parole = sum(freq.values())
    return tot_caratteri / tot_parole

testo = """Python è un linguaggio di programmazione molto potente.
Python è usato per analisi dati e sviluppo web.
Studiare Python è divertente!"""

pulito = pulisci_testo(testo)
print("Numero di parole:", conta_parole(pulito))

freq = frequenza_parole(pulito)
print("Frequenza parole:", freq)

print("Parole uniche:", parole_uniche(freq))
print("Top 5 parole:", top_n_parole(freq))
print("Lunghezza media:", round(lunghezza_media(freq), 2))
