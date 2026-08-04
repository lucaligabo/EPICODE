# Esercizio 1

A = {"Anna", "Luca", "Marco"}
B = {"Luca", "Sara", "Marco"}
print("Entrambi:", A & B)
print("Solo A:", A - B)
print("Totale unici:", len(A | B))


# Esercizio 2

A = {"Anna", "Luca", "Marco"}
B = {"Luca", "Sara", "Marco"}
print("Entrambi:", A & B)
print("Solo A:", A - B)
print("Totale unici:", len(A | B))


# Esercizio 3

import random
numeri = {random.randint(1, 20) for _ in range(10)}
print("Set casuale:", numeri)


#Esercizio 4

frase = "ciao come stai ciao tutto bene"
parole = frase.split()
conteggio = {}
for p in parole:
    conteggio[p] = conteggio.get(p, 0) + 1
print("Conteggio:", conteggio)


# Esercizio 5

d = {"a": 1, "b": 2, "c": 3}
inverso = {v: k for k, v in d.items()}
print("Inverso:", inverso)


# Esercizio 6

chiavi = ["nome", "età", "città"]
valori = ["Anna", 25, "Roma"]
d = dict(zip(chiavi, valori))
print("Dizionario:", d)


# Esercizio 7

parole = ["ciao", "come", "va", "oggi"]
gruppi = {}
for p in parole:
    gruppi.setdefault(len(p), []).append(p)
print("Raggruppate:", gruppi)


# Esercizio 8

testo = "programmazione"
freq = {}
for c in testo:
    freq[c] = freq.get(c, 0) + 1
print("Frequenza:", freq)