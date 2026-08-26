
import numpy as np
import random

random.seed(42)
np.random.seed(42) 

dati = np.random.randint(10,100,size=(6,5))
print ("Dati originali: \n",dati)

print ("\nForma: ", dati.shape) 
print ("Tipo di dato: ", dati.dtype)

print("\nPrima riga:", dati[0])
print("Prima colonna:", dati[:,0])
print("Sub-Matrice (prime 2 righe, prime 3 colonne): \n", dati[:2,:3])

view = dati[:2, :2]
copy = dati[:2, :2].copy()
view[0,0] = 999
print ("\nDopo la modifica della view:\n",dati)
print ("La copia resta invariata\n", copy)

reshaped = dati.reshape(3,10)
print("\nArray reshaped in 3x10:\n",reshaped)

print("\nIterazione su ogni elemento con 'nditer': ")
for x in np.nditer(dati):
    print(int(x),end=" ")
print()

extra = np.random.randint(10, 100, size=(6,2))
unito = np.hstack((dati,extra))
print("\nArray unito con nuove colonne:\n", unito)

split = np.split(unito,2)
print ("\nArray divisio in due blocchi:\n", split[0],"\n",split[1])

mask = dati > 50
print("\nValori > 50\n",dati[mask])

ordinati = np.sort(dati, axis=1)
print("\nOgni riga ordinata:\n", ordinati)

radici = np.sqrt(dati)
print("\nRadici quadrate di ogni elemento:\n", radici)

print("\nMedia per colonna:", np.mean(dati, axis=0))
print("Deviazione standard totale:", np.std(dati))