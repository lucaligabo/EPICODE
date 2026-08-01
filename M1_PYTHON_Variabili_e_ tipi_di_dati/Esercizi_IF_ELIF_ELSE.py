# Esercizio 1

x = -10

if x >= 0:
    print ("positivo")
else:
    print ("negativo")


# Esercizio 2

a = 10
b = 7 

if a > b:
    print ("a è maggiore di b")
else: 
    print ( "b è maggiore di a")


# Esercizio 3

età = 20 

if età >= 18:
    print ("sei maggiorenne")
else:
    print ("sei minorenne")


# Esercizio 4

n = 9
if n % 3 == 0:
    print("Multiplo di 3")
else:
    print("Non multiplo di 3")


# Esercizio 5 

voto = 22
if voto >= 18:
    print("Esame superato")
else:
    print("Bocciato")


# Esercizio 6 

c = "a"
if c in "aeiou":
    print("Vocale")
else:
    print("Consonante")


# Esercizio 7

x = 0
if x > 0:
    print("Positivo")
elif x < 0:
    print("Negativo")
else:
    print("Zero")


# Esercizio 8

a, b, c = 7, 3, 9
if a >= b and a >= c:
    print("a è il maggiore")
elif b >= a and b >= c:
    print("b è il maggiore")
else:
    print("c è il maggiore")


# Esercizio 9

eta = 70
if eta < 12:
    prezzo = 5
elif eta < 65:
    prezzo = 10
else:
    prezzo = 7
print("Prezzo biglietto:", prezzo, "€")


# Esercizio 10

a, b, c = 5, 5, 3
if a == b == c:
    print("Triangolo equilatero")
elif a == b or b == c or a == c:
    print("Triangolo isoscele")
else:
    print("Triangolo scaleno")
