# ESERCIZIO

# Creare una classe Persona con attributo "nome" e metodo presentati()
# Poi creare una sottoclasse Studente che aggiunge l'attributo "corso" e lo include nella presentazione.
# Infine, rendi l'attributo "nome" privato e permetti di leggerlo solo tramite un metodo dedicato.


# Creo la classe Persona con attributo "nome" e metodo presentati()

class Persona:
    def __init__(self, nome):
        self.nome = nome  # Attributo pubblico

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome}.")

# Creo la sottoclasse Studente che eredita da Persona e aggiunge l'attributo "corso"
class Studente(Persona):
    def __init__(self, nome, corso):
        super().__init__(nome)  # Chiamo il costruttore della classe base
        self.corso = corso  # Attributo specifico della sottoclasse

# Definisco il metodo presentati() che include il corso nella presentazione
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e sto studiando {self.corso}.") 

# Modifico l'attributo "nome" per renderlo privato e aggiungo un metodo getter per leggerlo
class Persona:
    def __init__(self, nome):
        self.__nome = nome  # Attributo privato

    def presentati(self):
        print(f"Ciao, mi chiamo {self.__nome}.")

    def get_nome(self):
        return self.__nome  # Metodo getter per leggere l'attributo privato


# N.B : La classe "Persona" è stata ridefinita per rendere l'attributo "nome" privato e aggiungere un metodo getter come da descrizione dell'esercizio.
#       Chiaro che la prima definizione della classe Persona non è più necessaria, ma è stata mantenuta per chiarezza e per mostrare l'evoluzione del codice.