# ESERCIZIO

# Immaginiamo due corsi universitari, Corso A e Corso B. Vogliamo Sapere:
# - Chi frequenta entrambi i corsi
# - Chi frequenta solo il Corso A
# - Chi frequenta solo il Corso B
# - Chi frequenta almeno un corso
# - Quanti studenti unici ci sono in totale

# Crea due tuple, una per il Corso A e una per il Corso B, contenenti i nomi degli studenti iscritti a ciascun corso. Poi utilizzia le operazioni sugli insiemi per ottenere le informazioni richieste.
corso_a = ("Alice", "Bob", "Charlie", "David")
corso_b = ("Charlie", "David", "Eve", "Frank")

# Converte le tuple in insiemi
insieme_a = set(corso_a)
insieme_b = set(corso_b)

# Chi frequenta entrambi i corsi
entrambi = insieme_a & insieme_b

# Chi frequenta solo il Corso A
solo_a = insieme_a - insieme_b

# Chi frequenta solo il Corso B
solo_b = insieme_b - insieme_a

# Chi frequenta almeno un corso
almeno_uno = insieme_a | insieme_b

# Quanti studenti unici ci sono in totale
studenti_unici = len(almeno_uno)

print("Chi frequenta entrambi i corsi:", entrambi)
print("Chi frequenta solo il Corso A:", solo_a)
print("Chi frequenta solo il Corso B:", solo_b)
print("Chi frequenta almeno un corso:", almeno_uno)
print("Numero di studenti unici:", studenti_unici)