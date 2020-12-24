'''Implementare l'algoritmo per il calcolo di un'eqazione di primo grado ax + b = 0'''

eq = input("Digitare l'equazione del tipo ax + b = 0: ")

indice_x = eq.index("x")
a = int(eq[:indice_x])

indice_piu = eq.index("+")
indice_uguale = eq.index("=")
b = int(eq[indice_piu + 1 : indice_uguale])

if a == 0 and b == 0:
    print("L'equazione è indeterminata")
elif a == 0 and b != 0:
    print("L'equazione è impossibile")
elif a != 0 and b == 0:
    print("x = 0")
elif b%a ==0:    
    print(-b/a)
else:
    print(-b, "/", a)