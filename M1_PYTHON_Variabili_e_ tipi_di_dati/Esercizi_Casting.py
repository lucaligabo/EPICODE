# Esercizio 1

n_int = 10
n_float = float(n_int)
print(n_int, n_float)


# Esercizio 2 

n_float = 9.7
n_int = int(n_float)
print(n_int)  


# Esercizio 3

n_str = "123"
n_int = int(n_str)
print(n_int)  


# Esercizio 4

num_str = "3.14"
num_float = float(num_str)
print(num_float)  


# Esercizio 5

n_str = "ciao"

try:
    num_int = int(n_str)

except ValueError:
    print("Non si può convertire 'ciao' in intero")




