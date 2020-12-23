'''A un concorso pubblico hanno partecipato due candidati di cui si conoscono i nomi e i punteggi conseguiti. Visualizza l'elenco dei due
candidati prima in ordine alfabetico e poi in ordine decrescente di punteggio.'''
candidati = []

candidato1 = input("Come si chiama il primo candidato? ")
candidato1 = str.title(candidato1)
candidati.append(candidato1)

candidato2 = input("E il secondo? ")
candidato2 = str.title(candidato2)
candidati.append(candidato2)

candidati.sort()

punteggio1 = int(input("Qual è il punteggio del primo candidato? "))
punteggio2 = int(input("E quello del secondo? "))

print (candidati)

if punteggio1 == punteggio2:
    print("Pareggio!")
elif punteggio1 > punteggio2:
    print(candidato1, ',', candidato2)
else:
    print(candidato2, ',', candidato1)
