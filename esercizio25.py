candidati = []
a = input("Come si chiama il primo candidato? ")
candidati.append(a)
b = input("E il secondo? ")
candidati.append(b)
#str.title(candidati)
candidati.sort()
c = int(input("Qual è il punteggio del primo candidato? "))
d = int(input("E quello del secondo? "))
print (candidati)
if c > d:
    print(a, ',', b)
else:
    print(b, ',', a)
