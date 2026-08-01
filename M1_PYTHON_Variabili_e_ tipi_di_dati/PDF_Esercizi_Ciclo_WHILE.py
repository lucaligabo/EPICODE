# ESERCIZIO

# Prova a scrivi un programma utilizzando il ciclo while che:
# 1. Chiede all'utente di inserire un numero intero positivo
# 2. Continua a chiedere finchè l'utente non inserisce un numero postivo (>0)
# 3. quando il numero è posttivo, stampa: "    Hai insertio un numero positivo: <numero>" e termina il programma

while True:
    numero = int(input("Inserisci un numero intero positivo: "))
    if numero > 0:
        print(f"Hai inserito un numero positivo: {numero}")
        break
    