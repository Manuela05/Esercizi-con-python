'''Convertire un numero binario in uno decimale ì. All'inizio richiedere il numero di cifre di cui è composto il numero binario (lunghezza);
richiedere le cifre del numero una a una a partire da destra e per ciascna calcolare il prodotto della cifra binaria per la potenza di 2
corrispondente alla posizione della cifra binaria e aggiunge il risultato alla "somma".'''

lunghezza = int(input("Da quante cifre è composto il numero? "))

posizione = 0
somma = 0

print("Inserire le cifre del numero binario una a una a partire da destra")

for i in range(lunghezza):
    cifra = int(input())
    addendo = 2**posizione*cifra
    somma += addendo
    posizione += 1

print(somma)

#La funzione di python per conversioni binario-decimale è int("numerobinario", base=2))
