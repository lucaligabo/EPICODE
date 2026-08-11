
# Classe che rappresenta un prodotto
class Product:
    def __init__(self, name: str, price: float):
        # nome del prodotto
        self.name = name
        # prezzo unitario
        self.price = price

    def __str__(self):
        # rappresentazione leggibile del prodotto
        return f"{self.name} - €{self.price:.2f}"

    def __eq__(self, other):
        # due prodotti sono uguali se hanno stesso nome e prezzo
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price


# Classe che rappresenta un carrello
class ShoppingCart:
    def __init__(self):
        # lista di prodotti
        self.items = []

    def add_product(self, product: Product):
        # aggiunge un prodotto al carrello
        self.items.append(product)

    def remove_product(self, product: Product):
        # rimuove un prodotto (se presente)
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
        # calcola il prezzo totale dei prodotti
        return sum(p.price for p in self.items)

    def __len__(self):
        # permette di usare len(cart) = numero di prodotti
        return len(self.items)

    def __str__(self):
        # rappresentazione leggibile del carrello
        if not self.items:
            return "Carrello vuoto"
        lines = ["Carrello:"]
        for p in self.items:
            lines.append(f"- {p}")
        lines.append(f"Totale: €{self.total_price():.2f}")
        return "\n".join(lines)

    def __add__(self, other):
        # unisce due carrelli creando un nuovo carrello
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart
    
    
    
    # Demo d’uso
if __name__ == "__main__":
    # creiamo alcuni prodotti
    penna = Product("Penna", 1.50)
    quaderno = Product("Quaderno", 2.30)
    zaino = Product("Zaino", 25.00)

    # creiamo due carrelli
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()

    # aggiungiamo prodotti
    cart1.add_product(penna)
    cart1.add_product(quaderno)
    cart2.add_product(zaino)

    # stampiamo i carrelli
    print("=== Carrello 1 ===")
    print(cart1)
    print("\n=== Carrello 2 ===")
    print(cart2)

    # uniamo i carrelli con l'overloading di +
    merged = cart1 + cart2
    print("\n=== Carrello Unito ===")
    print(merged)

    # rimuoviamo un prodotto
    cart1.remove_product(penna)
    print("\n=== Carrello 1 dopo rimozione ===")
    print(cart1)

    # lunghezza totale
    print("\nNumero di articoli in merged:", len(merged))