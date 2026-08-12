# ESERCIZIO 

# Crea una classe Divisione con un metodo dividi(a, b) che gestisca la divisione per zero
# Crea una classe Persona che sollevi un ValueError se l'età inserita è negativa
# Crea una classe Banca con metodo preleva(). Se il saldo non basta, solleva un eccezione personalizzata.

# Svolgimento

# ---- Il programma, naturalmente, si blocca dopo il primo ValueError che viene riscontrato (line 40 - commento line 39)
# ---- commentare line 40 per far continuare il programma con ultimo esercizio


# Creo una classe Divisione
class Divisione:
    # Creo metedo dividi() che gestica divisione per 0
    def dividi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Errore: non è possibile dividere per zero."

divisione = Divisione()

print(divisione.dividi(10, 2))  # 5.0
print(divisione.dividi(10, 0))  # Messaggio di errore


# Creo una classe Persona che solleva ValueErroe in caso di età negativa
class Persona:
    def __init__(self, eta):
        if eta < 0:
            raise ValueError("L'età non può essere negativa.")
        self.eta = eta


persona = Persona(25)
print(persona.eta)

# Solleva ValueError
persona_non_valida = Persona(-5)


# Creo classe Banca con metodo preleva(). Se il saldo non basta, solleva un eccezione personalizzata.

class SaldoInsufficienteError(Exception):
    pass


class Banca:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva(self, importo):
        if importo > self.saldo:
            raise SaldoInsufficienteError(
                "Impossibile effettuare il prelievo: saldo insufficiente."
            )

        if importo <= 0:
            raise ValueError("L'importo deve essere positivo.")

        self.saldo -= importo
        return self.saldo


conto = Banca(100)

try:
    print(conto.preleva(150))
except SaldoInsufficienteError as errore:
    print(errore)