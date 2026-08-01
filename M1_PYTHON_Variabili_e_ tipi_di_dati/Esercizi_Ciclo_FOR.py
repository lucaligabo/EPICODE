# Esercizio 1 

for i in range(1, 11):
    print(i)


# Esercizio 2

for i in range(2, 21, 2):
    print(i)


# Esercizio 3

parola = "Python"
for c in parola:
    print(c)


# Esercizio 4

somma = 0
for i in range(1, 101):
    somma += i
print("Somma =", somma)


# Esercizio 5

for i in range(1, 11):
    print(f"3 x {i} = {3*i}")


# Esercizio 6

n = 5
fattoriale = 1
for i in range(1, n+1):
    fattoriale *= i
print("Fattoriale =", fattoriale)


# Esercizio 7 

parola = "programmazione"
vocali = "aeiou"
conta = 0
for c in parola:
    if c in vocali:
        conta += 1
print("Numero di vocali:", conta)


# Esercizio 8 

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end="  ")
    print()


# Esercizio 9

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Esercizio 10

for i in range(1, 11):
    if i == 7:
        break
    print(i)
