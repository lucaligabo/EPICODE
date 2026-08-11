# ESERCIZIO

# Crea una classe Studente che abbia:
# - @classmethod per creare uno studente a partire da una stringe tipo "Luca-20-Matematica"
# - @property per calcolare automaticamente l'anno di nascita a partire dall'età
# - @property con setter per impedire età negative

#Svolgimento

from datetime import datetime


class Studente:
    def __init__(self, nome, eta, materia):     # Inizializzo i dati dello studente
        self.nome = nome
        self._eta = eta      # uso un attributo interno per salvare l'età
        self.materia = materia

    @classmethod
    def da_stringa(cls, testo):             # Creo uno studente partendo da una stringa nel formato:"nome-età-materia"
        nome, eta, materia = testo.split("-")
        return cls(nome, int(eta), materia)

    @property
    def eta(self):                  # Restituisce l'età corrente
        return self._eta

    @eta.setter
    def eta(self, valore):          # Controllo che non venga inserita età negativa, in caso segnalo con messaggio!
        if valore >= 0:
            self._eta = valore
        else:
            print("Errore! - Hai inserito un età negativa.")

    @property
    def anno_di_nascita(self):        # Calcolo l'anno di nascita usando l'anno corrente
        return datetime.now().year - self._eta



studente = Studente.da_stringa("Luca-20-Matematica")

print(studente.nome)              # Luca
print(studente.eta)               # 20
print(studente.anno_di_nascita)   # anno di nascita calcolato automaticamente

studente.eta = 25                 # aggiorno l'età tramite il setter, genera messaggio errore se negativa ma non blocca programma e non aggiorna età.
print(studente.eta)

