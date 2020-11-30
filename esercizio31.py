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