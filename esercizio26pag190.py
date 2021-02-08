'''I voti assegnati a 30 studenti sono memorizzati in un dizionario avente per chiavi le matricole e per valori i voti corrispondenti.
Elencare i numeri di matricola degli studenti che hanno ottenuto una votazione superiore alla media di tutte le votazioni.'''

studenti_voti = {100: 8, 101: 5, 102: 8, 103: 2, 104: 7, 105: 3, 106: 8, 107: 6, 108: 6, 109: 4, 110: 8, 111: 5, 112: 9, 113: 2, 114: 7, 115: 9,
                 116: 8, 117: 5, 118: 3, 119: 5, 120: 5, 121: 4, 122: 7, 123: 2, 124: 9, 125: 4, 126: 8, 127: 3, 128: 2, 129: 8}

studenti = list(studenti_voti.keys())
voti = list(studenti_voti.values())
media = round(sum(voti)/len(voti), 1)

stud_sopra_media = []
for e in range(len(voti)):
    if voti[e] > media:
        stud_sopra_media.append(studenti[e])
    

print(stud_sopra_media)