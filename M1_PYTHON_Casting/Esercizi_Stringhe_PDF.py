
# ESERCIZIO 

# Chiedi una frase e inverti l'ordine delle parole
frase = input("Inserisci una frase: ")

# Rimuove spazi, trasforma tutto in minuscolo e crea una stringa continua
frase_pulita = ''.join(frase.lower().split())

# Inverte la stringa pulita
frase_invertita = frase_pulita[::-1]

# Controllo del palindromo
if frase_pulita == frase_invertita:
    print("La frase è un palindromo!")
else:
    print("La frase non è un palindromo.")