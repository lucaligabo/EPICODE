import unittest
from src.Calcolatrice import somma

# Classe generale per testare funzioni calcolatrice
class Test_Calcolatrice(unittest.TestCase):
    # Funzione per testare somma, varie esempi
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)
        self.assertEqual(somma(1, 2, 3, 4), 10)
        self.assertEqual(somma(5), 5)
        self.assertEqual(somma(), 0)

if __name__ == '__main__':
    unittest.main()
