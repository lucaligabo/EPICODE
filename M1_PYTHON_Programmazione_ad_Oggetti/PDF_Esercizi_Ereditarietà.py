# ESERCIZIO

# Crea una classe Animale con attributo nome e metodo verso(). Poi crea due classi derivate:
# - Cane -> verso() stampa "Bau"
# - Gatto -> verso() stampa "Miao"
# Crea un oggetto di ciascuna classe e chiama il metodo verso().

# Svolgimento

# Creo Classe Animale
class Animale:
    def __init__(self,nome):
        self.nome = nome

    def verso(self):
        pass

# Creo Classe Cane
class Cane(Animale):
    def verso(self):
        print(f"{self.nome} dice: BAU")

# Creo Classe Gatto
class Gatto(Animale):
    def verso(self):
        print(f"{self.nome} dice: MIAO")

# Creo un oggetto di ciascuna classe
Animale1 = Cane("Fido")
Animale2 = Gatto("Chicca")

# Chiamo metodo verso()
Animale1.verso()
Animale2.verso()



