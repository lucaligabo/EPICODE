#Aggiungere un nuovo contatto (nome, numero, email).

#Modificare un contatto esistente.

#Eliminare un contatto.

#Cercare un contatto per nome.

#Visualizzare tutti i contatti in ordine alfabetico.



rubrica = []

# FUNZIONE PER AGGIUNGERE
def aggiungi_contatto (nome, numero, email):
    contatto = {"nome" : nome, "numero" : numero, "email" : email}
    rubrica.append(contatto)
    print (f"Contatto {nome} aggiunto!")

# FUNZIONE PER MODIFICARE
def modifica_contatto(nome, nuovo_numero = None, nuova_email = None):
    for c in rubrica:
        if c["nome"].lower() == nome.lower():
            if nuovo_numero:
                c["numero"] = nuovo_numero

            if nuova_email:
                c["email"] = nuova_email
            print(f"Contatto {nome} modificato!")
            return
    print("Contatto non trocato.")


# FUNZIONE PER ELIMINARE
def elimina_contatto(nome):
    for c in rubrica:
        if c["nome"].lower() == nome.lower():
            rubrica.remove(c)
            print(f"Contatto {nome} eliminato")
            return
    print("Contatto non trovato.")

# FUNZIONE PER CERCARE
def cerca_contatto(nome):
    for c in rubrica:
        if c["nome"].lower() == nome.lower():
            print("Contatto trovato", c)
            return
    print("Contatto non trovato")


# FUNZIONE PER MOSTRARE
def mostra_contatti():
    if not rubrica:
        print("Rubrica vuota!")
        return
    ordinati = sorted(rubrica, key=lambda x: x["nome"].lower())
    for c in ordinati:
        print(f"{c['nome']} - {c['numero']} - {c['email']}")
        

aggiungi_contatto("Luca", "3331234567", "luca@email.com")   
aggiungi_contatto("Anna", "3209876543", "anna@email.com")   
mostra_contatti()                                           

modifica_contatto("Luca", nuova_email="lucanuovo@email.com") 
cerca_contatto("Anna")                                      
elimina_contatto("Anna")                                    
mostra_contatti()                                           


