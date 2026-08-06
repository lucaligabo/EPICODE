# ESERCIZIO

# Crea una classe ContoBancario con:
# - Attributo privato __saldo
# - Metodo deposita(importo) che aggiunge soldi solo se > 0
# - Metodo preleva(importo) che riduce il saldo se sufficiente
# Simula alcune operazioni di deposito

# Svolgimento

# Creo una classe ContoBancario
class ContoBancario:
    def __init__(self, saldo_iniziale=0.0):    # Imposto saldo a 0.0 per iniziare 
        self.__saldo = float(saldo_iniziale)    # Attributo privato, impostato come float

    def deposita(self, importo):
        importo = float(importo)    # Attributo convertito in float
        if importo > 0:             # Controllo se importo depositato > 0
            self.__saldo += importo     
            print(f"Deposito di {importo:.2f} € effettuato con successo! - \nNuovo Saldo = {self.__saldo:.2f} €")       # Aumento saldo
        else:
            print("!!! - Errore - !!! \nL'importo deve essere maggiore di 0 €")

    def preleva(self, importo):
        importo = float(importo)    # Attributo convertito in float
        if importo <= 0:            # Controllo se importo prelevato < 0
            print("!!! - Errore - !!! \nL'importo deve essere maggiore di 0 €")
        elif importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di {importo:.2f} € effettuato con successo! - \nNuovo Saldo = {self.__saldo:.2f} €")
        else:
            print(f"!!! - Errore - !!! \nSALDO INSUFFICIENTE - Disponibilità: 0 €")

    def get_saldo(self):
        return self.__saldo

# Simulazione 

print("--- Creazione nuovo conto ---")
mio_conto = ContoBancario(100) # Conto creato con 100€ iniziali
print(f"Saldo iniziale: {mio_conto.get_saldo()}€\n")

print("--- Simulazione Depositi ---")
mio_conto.deposita(50)   # Deposito valido (+50€)
mio_conto.deposita(200)  # Deposito valido (+200€)
mio_conto.deposita(-30)  # Tentativo di deposito non valido (errore)

print("\n--- Simulazione Prelievi ---")
mio_conto.preleva(70)    # Prelievo valido (-70€)
mio_conto.preleva(500)   # Prelievo oltre il saldo (errore)
print(f"\nSaldo finale del conto: {mio_conto.get_saldo()}€")