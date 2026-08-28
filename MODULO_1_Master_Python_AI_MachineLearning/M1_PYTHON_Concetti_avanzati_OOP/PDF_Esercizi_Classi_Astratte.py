# ESERCIZIO

# Crea una classe astratta Veicolo con metodo astratto muovi().
# Poi crea due classi concrete:
# - Auto -> muovi() stampa "L'auto su muove su strada"
# - Aereo -> muovi() stampa "L'areo vola nel cielo"
# Infine , scrivi una funzione che accetti un generico Veicolo e chiami muovi()

from abc import ABC, abstractmethod

# Creo classe astratta Veicolo con metodo muovi()
class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
        pass

# Creo classe auto , definendo il metodo muovi()
class Auto(Veicolo):
    def muovi(self):
        print("L'auto si muove su strada")

# Creo classe aereo , definendo il metodo muovi()
class Aereo(Veicolo):
    def muovi(self):
        print("L'aereo vola nel cielo")

# Creo funzione "fai_muovere"
def fai_muovere(veicolo: Veicolo):
    veicolo.muovi()


fai_muovere(Auto())
fai_muovere(Aereo())
        