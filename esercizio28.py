partecipanti = []
lanci = []

print("Una volta inseriti i nomi di tutti i parteciapanti e i rispettivi lanci digitare stop")

while True:
    nomestudente = input("Inserire il nome dello studente: ")
    if nomestudente == "stop":
        break
    else:
        lancio = int(input("Inserire la lunghezza del suo lancio (in metri): "))
        nomestudente = str.title(nomestudente)
        partecipanti.append(nomestudente)
        lanci.append(lancio)

record = max(lanci)
indicelancio = lanci.index(record)
vincitore = partecipanti[indicelancio]
print("Il vincitore/vincitrice è", vincitore, "con un lancio di", record, "metri")