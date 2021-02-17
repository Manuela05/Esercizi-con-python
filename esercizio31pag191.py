'''La rete di vendita di un'azienda è suddivisa in 4 zone: Nord, Sud, Centro, Isole. Dopo aver acquisito in un array il fatturato nelle 4 zone
calcolare il totale del fatturato e i valori in percentuale delle vendite nelle 4 zone rispetto al totale'''

            fatturato = {}
            fatturato["fatt_nord"] = float(input("Fatturato zona Nord: "))
            fatturato["fatt_sud"] = float(input("Fatturato zona Sud: "))
            fatturato["fatt_centro"] = float(input("Fatturato zona Centro: "))
            fatturato["fatt_isole"] = float(input("Fatturato zona Isole: "))

            totale = round(sum(fatturato.values()), 1)

            perc_nord = fatturato["fatt_nord"]*100/totale
            perc_sud = fatturato["fatt_sud"]*100/totale
            perc_centro = fatturato["fatt_centro"]*100/totale
            perc_isole = fatturato["fatt_isole"]*100/totale
            print(totale)

            #print("Il totale è", totale)
            #print("Le percentuali delle varie zone rispetto al totale sono: Nord:", perc_nord, "%, Sud:", perc_sud, "%, Centro:", perc_centro, "%, Isole:", perc_isole, "%")
