'''I voti assegnati a 30 studenti sono memorizzati in un dizionario avente per chiavi le matricole e per valori i voti corrispondenti.
Elencare i voti in ordine crescente e successivamente visualizzare quali voti diversi sono stati assegnati riducendo a uno i voti uguaali.'''

studenti_voti = {100: 8, 101: 5, 102: 8, 103: 2, 104: 7, 105: 3, 106: 8, 107: 6, 108: 6, 109: 4, 110: 8, 111: 5, 112: 9, 113: 2, 114: 7, 115: 9,
                 116: 8, 117: 5, 118: 3, 119: 5, 120: 5, 121: 4, 122: 7, 123: 2, 124: 9, 125: 4, 126: 8, 127: 3, 128: 2, 129: 8}

studenti = list(studenti_voti.keys())
voti = list(studenti_voti.values())
voti_ordinati = voti[:]
voti_ordinati.sort()

voti_diversi = []
for i in range(min(voti), max(voti)):
    if i in voti:
        voti_diversi.append(i)

print(voti_ordinati)
print(voti_diversi)