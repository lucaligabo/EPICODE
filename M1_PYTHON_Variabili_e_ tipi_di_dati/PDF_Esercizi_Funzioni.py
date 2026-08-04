# ESERCIZIO

# Definisci una funzione chiamata "Media" che:
# - Riceve una lista di numeri come parametro
# - Calcola la media dei numeri nella lista
# nb: usa len() e sum() per renderela semplice, leggera ed efficace

# Definisco la funzione Media
def Media(lista_numeri):
    if len(lista_numeri) == 0:
        return 0  # Evito divisione per zero
    return sum(lista_numeri) / len(lista_numeri)

# Esempio di utilizzo della funzione Media
lista = [10, 20, 30, 40, 50]
media = Media(lista)
print("Media:", media)  