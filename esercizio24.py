'''Alla fine della giornata di elezioni per il ballottaggio tra due candidati, si acquisiscono i voti ottenuti dai due candidati. Scrivi il
programma che calcoli le percentuali ottenute da ciascun candidato e comunichi il nome  del vincitore'''

candidato1 = int(input("Inserire il numero di voti del primo candidato:"))
candidato2 = int(input("Inserire il numero di voti del secondo candidato:"))
totale = candidato1 + candidato2
perccandidato1 = candidato1*100/totale
perccandidato2 = candidato2*100/totale
if perccandidato1 == perccandidato2:
    print("Pareggio!")
elif perccandidato1 > perccandidato2:
    print("Il vincitore è il primo candidato!")
else:
    print("Il vincitore è il secondo candidato!")