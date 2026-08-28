# ESERCIZIO

# Scriti un programma che:
# - Ha una variabile età
# - Se l'età è minore di 18 stampa "Sei minorenne"
# - Se l'età è almeno 18 ma meno di 65 stampa "Sei adulto"
# - altrimenti stampa "Sei anziano"

età = int(input("Inserisci la tua età: "))

if età < 18:
    print("Sei minorenne")
elif età < 65:
    print("Sei adulto")
else:
    print("Sei anziano")