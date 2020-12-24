'''Creare un programma che, dati in input due numeri a e b, ne restituisca la differenza se il loro prodotto è > 10, la somma se
il loro prodotto è < o = 10'''

while True:
    a = float(input("Qual è il primo numero? "))
    if a == 00:
        break
    else:
        b = float(input("Qual è il secondo numero? "))
        prodotto = round(a*b, 1)
        if prodotto > 10:
            print("La differenza tra a e b è", a - b)
        else:
            print("La somma di a e b è", a + b)