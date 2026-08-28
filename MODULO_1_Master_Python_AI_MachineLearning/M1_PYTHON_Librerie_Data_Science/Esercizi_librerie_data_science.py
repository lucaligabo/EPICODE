# ESERCIZIO

# Crea un array con numeri da 1 a 10
# Calcola i quadrati e i cubi
# Organizza i dati in un DataFrame e visualliza un grafico a linee

# Svolgimento

# Importo le librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creo array con numeri da 1 a 10
arr = np.arange(1,11)

# Calcolo il quadrato e il cubo
quadrati = arr**2
cubi = arr**3

# Organizzo in DataFrame
df = pd.DataFrame({
    "Numero": arr,
    "Quadrato": quadrati,
    "Cubo": cubi  
})

print(df)

# Creo grafico

plt.plot(df["Numero"], df["Quadrato"], label="QUADRATI")
plt.plot(df["Numero"], df["Cubo"], label="CUBI")
plt.xlabel("Numero")
plt.ylabel("Valore")
plt.title("QUADRATI e CUBI")
plt.legend()
plt.show()