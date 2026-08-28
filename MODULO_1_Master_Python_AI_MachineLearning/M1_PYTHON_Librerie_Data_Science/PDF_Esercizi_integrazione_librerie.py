# ESERCIZIO

# Crea una serie di date (30 gg consecutivi)
# Genera valori casuali associati alle date
# Crea un DataFrame con indice temporale
# Fai un grafico a linea con i valori nel tempo


# Importo le librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Creo una serie di date
date_range = pd.date_range(start='2026-08-01', periods=31)

# Genero valori casuali per ogni data
valori_random = np.random.rand(31)

# Creo Dataframe
df = pd.DataFrame({'Data': date_range, 'Valori': valori_random})

# Traccio il grafico
df.set_index('Data').plot()
plt.show()

