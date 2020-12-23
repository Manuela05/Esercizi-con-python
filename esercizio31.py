'''Convertire un numero da decimale a binario. Dopo aver acquisito il valore del "Numero" da trasformare, si esegue la divisione del numero
per 2 e si calcola quoziente e resto. Il resto è la prima cifra della rappresentazione binaria. Si ripete il procedimento assegnando il
quoziente ottenuto a "Numero" e ricalcolando la divisione per 2; la ripetizione prosegue mentre il quoziente ottenuto si mantiene diverso da 0.
La rappresentazione binaria del numero decimale è costituita dalle cifre ottenute come resti lette in ordine inverso.'''

numero = int(input("Qual è il numero da convertire? "))

binario = []

dividendo = numero

while dividendo != 0:
    quoziente = int(dividendo/2)
    resto = dividendo%2
    resto = str(resto)
    binario.append(resto)
    dividendo = quoziente

binario.reverse()
print("".join(binario))