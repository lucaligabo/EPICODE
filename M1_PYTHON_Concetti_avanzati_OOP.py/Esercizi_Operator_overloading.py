# ESERCIZIO

# Creare un sistema per gestire conti bancari diversi, sfruttando classi astratte, ereditarietà, polimorfismo, property, decoratori e operator overloading.

from abc import ABC, abstractmethod

# Creazione classe astratta CONTO()
class Conto(ABC):
    

    def __init__(self, intestatario, saldo_iniziale = 0):
        self._intestatario = intestatario
        self._saldo = saldo_iniziale

    @property
    def saldo(self):
        return self._saldo
    
    @staticmethod
    def valida_importo(importo):
        return importo > 0
    
    @abstractmethod
    def deposita(self, importo):
        pass

    def preleva(self, importo):
        pass

    def __str__(self):
        return f"Conto di {self._intestatario} - Saldo: {self._saldo:.2f}$"
    
# Creazione classe ContoCorrente che eredita da Conto con e richiama le varia funzioni dichiarandole
class ContoCorrente(Conto):

    COMMISSIONE = 1.5   
    
    def deposita(self, importo):
        if self.valida_importo(importo):
            self._saldo += importo
        else:
            print ("Importo non valido per il deposito!")
    

    def preleva(self, importo):
        totale = importo + ContoCorrente.COMMISSIONE
        if self.valida_importo(importo) and self._saldo >= totale:
            self._saldo -= totale
        else:
            print("Saldo insufficente o importo non valido!")

    def __add__(self, altro):
        nuovo_saldo = self._saldo + altro._saldo
        return ContoCorrente(f"{self._intestatario} & {altro._intestatario}", nuovo_saldo)
    


if __name__ == "__main__":
    cc1 = ContoCorrente("Luca", 1000)
    cc2 = ContoCorrente("Giulia", 500)
    

# Operazioni di base
cc1.deposita(200)
cc1.preleva(50)
print(cc1)

# Fusione conti
conto_fuso = cc1 + cc2
print(conto_fuso)