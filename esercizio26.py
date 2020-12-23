'''Calcola la media degli stipendi dei dipendenti di un'azienda, acquisiti con una ripetizione fino a quando si inserisce il valore -1 per
segnalare la fine dell'input dei dati'''

print("Per fermare il programma digitare -1")

valori = []

while True:
    stipendio = int(input("Digitare l'importo dello stipendio "))
    if stipendio == -1:
        break
    else:
        valori.append(stipendio)

somma = sum(valori)
n_valori = len(valori)
media = somma/n_valori
print(media)