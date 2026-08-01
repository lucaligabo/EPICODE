# --- ESERCIZIO 1 ---
# Crea una variabile con il tuo nome e stampala

nome = "Luca"
cognome = "Ligabò"

print(nome, cognome)


#--- ESERCIZIO 2 ---
# Chiedi all'utente la sua età e stampala raddoppiata

while True:
    # 1. Chiede l'input all'utente
    eta_testo = input("Inserisci la tua età: ")
    
    try:
        # 2. Tenta di convertire in numero intero
        eta = int(eta_testo)
        
        # Controllo extra: l'età non può essere negativa
        if eta < 0:
            print("L'età non può essere un numero negativo! Riprova.")
            continue  # Ritorna all'inizio del ciclo while
            
        # Se la conversione riesce ed è valida, esce dal ciclo
        break
        
    except ValueError:
        # 3. Gestisce l'errore se l'utente scrive lettere o numeri con la virgola
        print("Errore! Devi inserire un numero intero (es. 25). Non usare lettere o virgole.")

# 4. Una volta usciti dal ciclo, esegue il calcolo e stampa
eta_raddoppiata = eta * 2
print(f"Perfetto! Il doppio della tua età è: {eta_raddoppiata}")


#--- ESERCIZIO 3 ---
# Crea due numeri e stampa la loro somma

# Option 1
n1 = 5
n2 = 7

print (n1 + n2)

# Option 2
n1 = 5
n2 = 7

Somma = n1 + n2 # Creo una variabile somma

print (Somma)