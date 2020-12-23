'''Scrivere un programma a cui viene passata una parola e riconosce se si tratta di un palindromo oppure meno'''

parola = input("Digitare una parola ")
inverso = parola[::-1]
if parola == inverso:
    print(parola, "è un palindromo")
else:
    print(parola, "non è un palindromo")
