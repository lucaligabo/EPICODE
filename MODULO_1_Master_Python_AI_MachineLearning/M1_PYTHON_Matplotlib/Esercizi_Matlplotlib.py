import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Creiamo un dataset fittizio
# -----------------------------

# Date mensili per il 2023
date = pd.date_range("2023-01-01", periods=12, freq="ME")

# Valori delle vendite (in migliaia di euro)
vendite = [10, 12, 15, 20, 25, 22, 24, 30, 28, 27, 32, 35]

# Età casuali di 50 clienti
np.random.seed(42)  # per avere sempre gli stessi risultati
eta_clienti = np.random.randint(18, 65, 50)

# Spesa media dei clienti (leggermente correlata all'età)
spesa_media = eta_clienti * 2 + np.random.randint(-20, 20, 50)


# -----------------------------
# 2. Grafico temporale vendite
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(date, vendite, marker="o", color="blue", linewidth=2, linestyle="--", label="Vendite")
plt.title("Andamento vendite mensili - 2023")
plt.xlabel("Mese")
plt.ylabel("Vendite (migliaia €)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()


# -----------------------------
# 3. Istogramma età clienti
# -----------------------------
plt.figure(figsize=(7,5))
plt.hist(eta_clienti, bins=8, color="skyblue", edgecolor="black", alpha=0.8)
plt.title("Distribuzione età dei clienti")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.show()


# -----------------------------
# 4. Grafico a dispersione
# -----------------------------
plt.figure(figsize=(7,5))
plt.scatter(eta_clienti, spesa_media, color="red", marker="o", alpha=0.7)
plt.title("Relazione tra età e spesa media")
plt.xlabel("Età dei clienti")
plt.ylabel("Spesa media (€)")
plt.grid(True, alpha=0.5)
plt.show()


# -----------------------------
# 5. Subplot multipli
# -----------------------------
fig, ax = plt.subplots(2,2, figsize=(10,8))

# Vendite nel tempo
ax[0,0].plot(date, vendite, marker="o", color="blue")
ax[0,0].set_title("Vendite mensili")

# Istogramma età
ax[0,1].hist(eta_clienti, bins=8, color="orange", edgecolor="black")
ax[0,1].set_title("Distribuzione età")

# Scatter plot età vs spesa
ax[1,0].scatter(eta_clienti, spesa_media, color="green", alpha=0.7)
ax[1,0].set_title("Età vs Spesa")

# Grafico ad area cumulativa vendite
vendite_cumulative = np.cumsum(vendite)
ax[1,1].fill_between(date, vendite_cumulative, color="lightblue", alpha=0.6)
ax[1,1].plot(date, vendite_cumulative, color="blue")
ax[1,1].set_title("Vendite cumulative")

# Miglioriamo layout
plt.tight_layout()
plt.show()