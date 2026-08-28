# PROGETTO 3 - MODOLUO 1

# Un’agenzia di viaggi online vuole realizzare un sistema informatico per gestire le prenotazioni dei clienti.
# Il sistema deve permettere di:
# - memorizzare le informazioni dei clienti e dei viaggi prenotati,
# - calcolare statistiche sulle vendite,
# - analizzare i dati con strumenti avanzati,
# - visualizzare i risultati in forma grafica. 


# SVOLGIMENTO

import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mostra i valori float di Pandas con due cifre decimali nell'output.
pd.options.display.float_format = "{:.2f}".format


# =========================================================
# PARTE 1 - Variabili e tipi di dati
# =========================================================

nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

destinazioni = ["Roma", "Parigi", "New York", "Tokyo", "Amsterdam", "Londra", "Dubai"]

prezzi_viaggio = {
    "Roma": 350.0,
    "Parigi": 520.0,
    "New York": 900.0,
    "Tokyo": 1100.0,
    "Amsterdam": 480.0,
    "Londra": 600.0,
    "Dubai": 750.0
}


# =========================================================
# PARTE 2 - Programmazione ad Oggetti (OOP)
# =========================================================

# Creo classe Cliente con realtivi attributi e metodo
class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    # Metodo per stampare le info del cliente
    def informazioni(self):
        print(f"Nome: {self.nome}")
        print(f"Età: {self.eta}")
        print(f"VIP: {'Sì' if self.vip else 'No'}")

# Creo classe Viaggio con relativi attributi
class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_giorni = durata_giorni

# Creo classe Prenotazione con relativi attributi e meteodo
class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    # Metodo per calcolare sconto se membro Vip
    def importo_finale(self):
        costo = self.viaggio.prezzo
        if self.cliente.vip:
            costo *= 0.90  # sconto del 10%
        return costo

    # Metodo per stampare le info della Prenotazione
    def dettagli(self):
        print("===== Dettagli prenotazione =====")
        self.cliente.informazioni()
        print(f"Destinazione: {self.viaggio.destinazione}")
        print(f"Prezzo base: {self.viaggio.prezzo:.2f} €")
        print(f"Durata: {self.viaggio.durata_giorni} giorni")
        print(f"Importo finale: {self.importo_finale():.2f} €")
        print("================================")


# Esempio base
cliente1 = Cliente(nome, eta, vip)
viaggio1 = Viaggio("Amsterdam", 600, 5)
prenotazione1 = Prenotazione(cliente1, viaggio1)
print("\nEsempio prenotazione:")
prenotazione1.dettagli()


# =========================================================
# PARTE 3 - NumPy
# =========================================================

# Genero 100 prenotazioni simulate con funzione random di Phyton
prenotazioni = []
nomi_clienti = ["Luca", "Anna", "Marco", "Giulia", "Paolo"]

for i in range(100):
    cliente = Cliente(random.choice(nomi_clienti), random.randint(18, 80), random.choice([True, False]))
    destinazione = random.choice(destinazioni)
    prezzo = random.uniform(200, 2000)
    durata = random.randint(2, 15)
    viaggio = Viaggio(destinazione, prezzo, durata)
    prenotazioni.append(Prenotazione(cliente, viaggio))

# Creo l'array con 100 prenotazioni simulate sopra
prezzi = np.array([p.viaggio.prezzo for p in prenotazioni])

# Calcolo le statistiche richiesta
prezzo_medio = np.mean(prezzi)
prezzo_minimo = np.min(prezzi)
prezzo_massimo = np.max(prezzi)
deviazione_standard = np.std(prezzi)
sopra_media = prezzi[prezzi > prezzo_medio]
percentuale_sopra_media = (len(sopra_media) / len(prezzi)) * 100

# Stampo a video i risultati delle statistiche
print("\nStatistiche sulle prenotazioni simulate:")
print(f"Prezzo medio: {prezzo_medio:.2f} €")
print(f"Prezzo minimo: {prezzo_minimo:.2f} €")
print(f"Prezzo massimo: {prezzo_massimo:.2f} €")
print(f"Deviazione standard: {deviazione_standard:.2f}")
print(f"Percentuale prenotazioni sopra la media: {percentuale_sopra_media:.2f}%")


# =========================================================
# PARTE 4 - Pandas
# =========================================================

# Genero un DataFrame con le colonne richieste
records = []

data_inizio = datetime(2026, 1, 1)
for i, pren in enumerate(prenotazioni):
    giorno_partenza = data_inizio + timedelta(days=i)
    incasso = pren.importo_finale()

    records.append({
        "Cliente": pren.cliente.nome,
        "Destinazione": pren.viaggio.destinazione,
        "Prezzo": pren.viaggio.prezzo,
        "Giorno_Partenza": giorno_partenza,
        "Durata": pren.viaggio.durata_giorni,
        "Incasso": incasso
    })

df = pd.DataFrame(records)

# Incasso totale dell'agenzia
incasso_totale = df["Incasso"].sum()

# Incasso medio per destinazione
incasso_medio_per_destinazione = df.groupby("Destinazione")["Incasso"].mean()

# Top 3 destinazioni più vendute
top_3_destinazioni = df["Destinazione"].value_counts().head(3)

print(f"\nIncasso totale dell'agenzia: {incasso_totale:.2f} €")
print("Incasso medio per destinazione:")
print(incasso_medio_per_destinazione)
print("Top 3 destinazioni più vendute:")
print(top_3_destinazioni)


# =========================================================
# PARTE 5 - Matplotlib
# =========================================================

# Grafico a barre: incasso per destinazione
incasso_per_destinazione = df.groupby("Destinazione")["Incasso"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(incasso_per_destinazione.index, incasso_per_destinazione.values, color="skyblue")
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2) Grafico a linee: andamento giornaliero degli incassi
andamento_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()

plt.figure(figsize=(10, 5))
plt.plot(andamento_giornaliero.index, andamento_giornaliero.values, marker="o", color="green")
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Giorno partenza")
plt.ylabel("Incasso (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3) Grafico a torta: percentuale di vendite per destinazione
vendite_per_destinazione = df["Destinazione"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(vendite_per_destinazione.values, labels=vendite_per_destinazione.index, autopct="%1.1f%%")
plt.title("Percentuale di vendite per destinazione")
plt.tight_layout()
plt.show()


# =========================================================
# PARTE 6 - Analisi avanzata
# =========================================================

# Creai dizionario per classificare le destinazioni per continente
categorie = {
    "Europa": ["Roma", "Parigi", "Amsterdam", "Londra"],
    "Asia": ["Tokyo", "Dubai"],
    "America": ["New York"],
    "Africa": []
}

# Creo colonna Categoria
categoria_per_destinazione = {}
for continente, cities in categorie.items():
    for city in cities:
        categoria_per_destinazione[city] = continente

# Se una destinazione non è stata mappata, assegno "Altro"
df["Categoria"] = df["Destinazione"].map(categoria_per_destinazione).fillna("Altro")

# Incasso totale per categoria
incasso_per_categoria = df.groupby("Categoria")["Incasso"].sum()

# Durata media dei viaggi per categoria
durata_media_per_categoria = df.groupby("Categoria")["Durata"].mean()

print("\nAnalisi avanzata:")
print("Incasso totale per categoria:")
print(incasso_per_categoria)
print("Durata media per categoria:")
print(durata_media_per_categoria)

# Salvataggio CSV
df.to_csv("prenotazioni_analizzate.csv", index=False)
print("\nFile salvato: prenotazioni_analizzate.csv")


# =========================================================
# PARTE 7 - Estensioni
# =========================================================

# Creo funzione clienti con più prenotazioni
def clienti_con_piu_prenotazioni(df, n):
    conteggio = df["Cliente"].value_counts()
    return conteggio.head(n)

print("\nClienti con più prenotazioni:")
print(clienti_con_piu_prenotazioni(df, 5))

# Grafico combinato: barre = incasso medio per categoria, linea = durata media per categoria
categoria_media_incasso = df.groupby("Categoria")["Incasso"].mean()
categoria_media_durata = df.groupby("Categoria")["Durata"].mean()

x = categoria_media_incasso.index
y1 = categoria_media_incasso.values
y2 = categoria_media_durata.values

fig, ax1 = plt.subplots(figsize=(10, 5))

color = "tab:blue"
ax1.bar(x, y1, color=color, alpha=0.7, label="Incasso medio per categoria")
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso medio (€)", color=color)
ax1.tick_params(axis="y", labelcolor=color)

ax2 = ax1.twinx()
color2 = "tab:red"
ax2.plot(x, y2, color=color2, marker="o", label="Durata media per categoria")
ax2.set_ylabel("Durata media (giorni)", color=color2)
ax2.tick_params(axis="y", labelcolor=color2)

plt.title("Incasso medio e durata media per categoria")
fig.tight_layout()
plt.savefig("Incasso_durata_media.png")
plt.show()