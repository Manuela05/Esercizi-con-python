def media(numeri):
    return round(sum(numeri) / len(numeri))

studenti_voti = {"Hemingway": [20, 18, 17], "Allan Poe": [23, 20, 22], "Whitman": [24, 30, 26], "Moore": [18, 22, 24]}

def suddivisione_studenti(dizionario):
    valori = list(dizionario.values())
    chiavi = list(dizionario.keys())

    for l in range(len(valori)):
        valori[l] = media(valori[l])

    media_studenti = {}

    k1 = []
    k2 = []
    k3 = []

    for i in range(len(valori)):
        
        if 18 <= valori[i] <= 23:
            k1.append(chiavi[i])
        
        elif 23 < valori[i] <= 26:
            k2.append(chiavi[i])
        
        else:
            k3.append(chiavi[i])

    media_studenti["18-23"] = k1
    media_studenti["24-26"] = k2
    media_studenti["27-30"] = k3
    
    return media_studenti


print(suddivisione_studenti(studenti_voti).items())
