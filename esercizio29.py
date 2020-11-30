valore = int(input("Qual è il valore di escursione termica prefissato? "))

cittàselezionate = []
contatore = 0

while True:
    città = input("Qual è il nome della città: ")
    if città == "fine":
        break
    else:
        città = str.title(città)
        tempmax = int(input("Qual è la temperatura massima registrata? "))
        tempmin = int(input("Qual è la temperatura minima registrata?"))
        escursione = tempmax - tempmin
        if escursione > valore:
            contatore += 1
            cittàselezionate.append(città)

print("Le città in cui si è verificata un'escursione termica di almeno", valore, "gradi, sono in tutto", contatore, ":", ", ".join(cittàselezionate))