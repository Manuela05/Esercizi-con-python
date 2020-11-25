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