'''Scrivi un programma che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la
lunghezza delle parole contenute in A.'''

n = int(input("Quante parole si vogliono inserire? "))
A = []
B = []
print("Dopo aver digitato ogni parola premere invio")
for i in range(n):
    parola = input()
    A.append(parola)
    B.append(len(parola))
print(B)


