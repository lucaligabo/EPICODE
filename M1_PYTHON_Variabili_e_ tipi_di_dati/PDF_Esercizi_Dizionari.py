# ESERCIZIO

# Crea un dizionario che rappresenti uno studente con le seguenti chiavi: "nome", "età" e "corso". Poi:
# - Modifica il volore di "età"
# - Aggiungi una nuova chiave "matricola"
# - Usa get() per recuperare un volore sconosciuto senza errore
# - Itera su tutte le coppie chiave-valore e stampale

# Crea un dizionario con le chiavi/valori iniziali
studente = {
    "nome": "Luca",
    "età": 38,
    "corso": "Epicode Master Python, AI & Machine Learning"
}

# Modifica il valore di "età"
studente["età"] = 39

# Aggiunge una nuova chiave "matricola"
studente["matricola"] = "123666"

# Usa get() per recuperare un valore sconosciuto senza errore
valore_sconosciuto = studente.get("indirizzo", "Indirizzo non disponibile")

# Itera su tutte le coppie chiave-valore e stampale
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")