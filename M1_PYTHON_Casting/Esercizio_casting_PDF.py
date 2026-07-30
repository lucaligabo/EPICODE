# ESERCIZIO

try:
    # 1. Chiede all'utente di inserire un numero intero
    input_utente = input("Inserisci un numero intero: ")
    numero_intero = int(input_utente)

    # 2. Converte il numero in decimale (float) e lo stampa
    numero_float = float(numero_intero)
    
    # 3. Converte il numero in stringa e lo stampa con un messaggio
    numero_stringa = str(numero_intero)
    print("Il numero convertito in stringa è: " + numero_stringa)

except ValueError:
    print("Errore: non hai inserito un numero intero valido!")
