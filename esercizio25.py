candidati = []
candidato1 = input("Come si chiama il primo candidato? ")
candidati.append(candidato1)
candidato2 = input("E il secondo? ")
candidati.append(candidato2)
#str.title(candidati)
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
