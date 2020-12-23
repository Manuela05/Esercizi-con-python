'''Dato un elenco di città, con l'indicazione per ciascuna  di esse del nome e delle temperature massima e minima registrate in un giorno,
si devono contare quante città hanno superato nel giorno un valore di escursione termica dato dall'utente.'''

valore = int(input("Qual è il valore di escursione termica prefissato? "))

cittàselezionate = []
contatore = 0
print("Una volta inserite tutte le città e i rispettivi dati digitare fine")
while True:
    città = input("Nome della città: ")
    if città == "fine":
        break
    else:
        città = str.title(città)
        tempmax = int(input("Temperatura massima registrata: "))
        tempmin = int(input("Temperatura minima registrata: "))
        escursione = tempmax - tempmin
        if escursione > valore:
            contatore += 1
            cittàselezionate.append(città)

print("Le città in cui si è verificata un'escursione termica di almeno", valore, "gradi, sono in tutto", contatore, ":", ", ".join(cittàselezionate))