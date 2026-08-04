# Esercizio 1

tuples = [(1, 3), (2, 1), (5, 0)]
ordinata = sorted(tuples, key=lambda x: x[1])
print("Ordinata:", ordinata)


# Esercizio 2

t = (1, 2, 3, 4, 5, 6)
pari = tuple([x for x in t if x % 2 == 0])
print("Numeri pari:", pari)


# Esercizio 3

t = (1, 2, 3, 4)
invertita = tuple(reversed(t))
print("Invertita:", invertita)


# Esercizio 4

s = "programmazione"
t = tuple(set(s))
print("Tupla caratteri unici:", t)


# Esercizio 5

a = [1, 2, 3]
b = ["a", "b", "c"]
zipped = list(zip(a, b))
print("Zip:", zipped)


# Esercizio 6

A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6}
diff = A ^ B ^ C
print("Diff simmetrica:", diff)

 
# Esercizio 7

frase = "ciao come stai ciao tutto bene"
uniche = set(frase.split())
print("Parole uniche:", uniche)


# Esercizio 8

liste = [[1, 2, 3], [3, 4, 5], [6, 7]]
unione = set().union(*map(set, liste))
print("Unione:", unione)
