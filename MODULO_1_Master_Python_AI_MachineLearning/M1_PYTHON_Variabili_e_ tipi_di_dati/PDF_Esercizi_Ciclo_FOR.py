# ESERCIZIO

# Scrivi un programma che:
# 1. Ha una lista di nomi
# 2. Stamapa ogni nome preceduto dal proprio numero d'ordine (es. 1. Alice)
# 3. Usa enumerate() per ottenere numero e nome

nomi = ["Alice", "Martin", "Gianfranco", "Luca", "Giulia"]

for numero, nome in enumerate(nomi, start=1):
    print(f"{numero}. {nome}")
    