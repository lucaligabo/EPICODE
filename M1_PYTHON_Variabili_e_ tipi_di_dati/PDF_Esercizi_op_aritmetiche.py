# ESERCIZIO
#  Chiedere all'utente quanti euro ha.

Saldo = float(input("Quanti € hai?: € "))

# Chiedere il prezzo di un singolo oggetto.

Unit_cost = float(input("Quanto costa un singolo oggetto?: "))

# Usare // per calcolare quante unità può comprare

Unit_cart = Saldo // Unit_cost
Cart_change = Saldo % Unit_cost

print(f"\nCon il tuo Saldo di: €{Saldo}, puoi comprare: {Unit_cart} oggetti.")
print(f"Ti restano ancora: € {Cart_change}.")