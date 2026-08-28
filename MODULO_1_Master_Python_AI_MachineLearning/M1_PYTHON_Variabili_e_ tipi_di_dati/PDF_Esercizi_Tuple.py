# ESERCIZIO

# Crea una tupla con 3 colori
# - Stampa il primo e l'ultimo
# - Conta quante volte compare un colore

# Creazione della tupla con 3 colori
colori = ("rosso", "verde", "blu")

# Stampa il primo e l'ultimo colore
print("Primo colore:", colori[0])
print("Ultimo colore:", colori[-1]) 

# Conta quante volte compare un colore specifico
color_count = "verde"
conteggio = colori.count(color_count)
print(f"Il colore {color_count} compare {conteggio} volta/e.")