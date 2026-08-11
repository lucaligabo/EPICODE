
# Scrivi una classe Calcolatrice con un metodo dividi(a, b) che gestisca la divisione per zero.

class Calcolatrice:
    def dividi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Errore: divisione per zero non consentita.")
            return None

# Demo
calc = Calcolatrice()
print(calc.dividi(10, 2))   # 5.0
print(calc.dividi(10, 0))   # Messaggio di errore


# Crea una classe Persona che accetta nome ed età. Se l’età è negativa, solleva un’eccezione standard (ValueError).

class Persona:
    def __init__(self, nome, eta):
        if eta < 0:
            raise ValueError("L'età non può essere negativa!")
        self.nome = nome
        self.eta = eta

# Demo
try:
    p1 = Persona("Mario", 25)
    print("Persona creata:", p1.nome, p1.eta)
    p2 = Persona("Anna", -3)  # Solleva ValueError
except ValueError as e:
    print("Errore:", e)


# Definisci una classe EtàNonValidaError e usala nella classe Studente quando l’età inserita non è realistica (< 0 o > 120).

class EtaNonValidaError (Exception):
   
 pass

class Studente:
    def __init__(self, nome, eta):
        if eta < 0 or eta > 120:
            raise EtaNonValidaError(f"Età non valida: {eta}")
        self.nome = nome
        self.eta = eta

try:
    s1 = Studente ("Luca ", 20)
    print ("Studente creato: ", s1.nome, s1.eta)
    s2 = Studente ("Paolo", 150)
except EtaNonValidaError as e:
    print("Errore:", e)


