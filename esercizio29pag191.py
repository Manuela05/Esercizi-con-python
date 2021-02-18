'''Scrivere un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la tassazione media'''

fasce = {15000: (0, 0, 23), 28000: (15001, 3450, 27), 55000: (28001, 6960, 38), 75000: (55001, 17220, 41), 10**12: (75001, 25420, 43)}

reddito = round(float(input("Reddito: ")))
for k in fasce:
    fascia = list(fasce[k])
    if fascia[0] < reddito < k:
        extra = reddito - fascia[0]
        imposta = round(extra*fascia[2]/100 + fascia[1])
tass_media = round(imposta/reddito*100, 2)
print(imposta)
print(tass_media, "%")  


