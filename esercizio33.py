'''Utilizzare una struttura acoda per memorizzare i nomi dei pazienti. Scrivere un programma per registraare i nomi. Visualizzare il nome
del primo paziente della coda'''

elenco = []
while True:
    paziente = input("Nome paziente: ").capitalize()
    if paziente == "Stop":
        break
    else:
        elenco.append(paziente)

indice = 0
while indice < len(elenco):
    prossimo = elenco.pop(indice)
    print("Deve sottoporsi all'esame ", prossimo)
indice += 1
    
print("Non ci sono altri pazienti in coda")