'''Verificare se un numero è pari o dispari'''

while True:
    try:
        numero = int(input("Numero: "))

        if numero%2 == 0:
            print(numero, "è un numero pari")
        else:
            print(numero, "è un numero dispari")
            break
    except ValueError:
        print("Inserire un numero intero")