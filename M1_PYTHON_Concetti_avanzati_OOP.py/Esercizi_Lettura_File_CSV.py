# Esercizio 1 

import csv

# 1. Creiamo un file CSV
with open("studenti.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "età", "corso"])
    writer.writerow(["Luca", 20, "Informatica"])
    writer.writerow(["Anna", 22, "Matematica"])
    writer.writerow(["Paolo", 19, "Fisica"])

# 2. Leggiamo il file CSV
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)


# Esercizio 2

import csv

with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for riga in reader:
        print(f"Nome: {riga['nome']}, Corso: {riga['corso']}")


# Esercizio 3 

import csv

with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for riga in reader:
        if riga["corso"] == "Informatica":
            print(riga["nome"], riga["età"])


# Esercizio 4 

import csv

with open("studenti.csv", "r", encoding="utf-8") as f_in, \
     open("maggiorenni.csv", "w", newline="", encoding="utf-8") as f_out:
    
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=["nome", "età", "corso"])
    writer.writeheader()

    for riga in reader:
        if int(riga["età"]) >= 21:
            writer.writerow(riga)

print("Creato maggiorenni.csv con gli studenti di 21 anni o più.")
