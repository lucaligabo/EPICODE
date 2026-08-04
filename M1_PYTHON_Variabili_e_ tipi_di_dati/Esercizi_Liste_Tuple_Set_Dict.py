# Esercizio 1 

numeri = [12, 7, 9, 18, 24, 5, 2]
somma_pari = sum([n for n in numeri if n % 2 == 0])
print("Somma dei pari:", somma_pari)


# Esercizio 2 

lista = [1, 2, 2, 3, 4, 4, 5]
senza_dup = []
for x in lista:
    if x not in senza_dup:
        senza_dup.append(x)
print("Lista senza duplicati:", senza_dup)


# Esercizio 3

lista = [1, 2, 3, 4, 5]
k = 2
rotata = lista[-k:] + lista[:-k]
print("Lista ruotata:", rotata)


# Esercizio 4 

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersezione = [x for x in a if x in b]
print("Intersezione:", intersezione)


# Esercizio 5 

coppie = [("a", 1), ("b", 2), ("c", 3)]
diz = dict(coppie)
print("Dizionario:", diz)


# Esercizio 6 

tuples = [(1, 2), (3, 4), (5, 6)]
somma = sum([sum(t) for t in tuples])
print("Somma:", somma)


# Esercizio 7 

numeri = [12, 3, 45, 7, 9]
risultato = (min(numeri), max(numeri))
print("Min e Max:", risultato)

