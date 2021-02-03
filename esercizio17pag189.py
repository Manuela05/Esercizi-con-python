'''Creare 2 liste contenenti l'una delle nazioni e l'altra le capitali corrispondenti nella medesima posizione; dopo aver chiesto una nazione
all'utente restituirne la capitale. Segnalare se la nazione non è presente nell'elenco'''

lista_naz = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaigian","Belgio", "Bielorussia","Bosnia ed Erzegovina", "Bulgaria","Cipro",
             "Croazia", "Danimarca", "Eire","Estonia", "Finlandia","Francia", "Germnania","Grecia","Islanda", "Italia","Kazakistan"]
lista_cap = ["Tirana", "Andorra la Vella", "Erevan", "Vienna", "Baku","Bruxelles", "Minsk","Sarajevo", "Sofia","Nicosia", "Zagabria",
             "Copenaghen", "Dublino","Tallinn", "Helsinki","Parigi", "Berlino", "Atene", "Reykjavik", "Roma","Nur-Sultan"]

d_naz_cap = {}
for i in range(len(lista_naz)):
    d_naz_cap[lista_naz[i]] = lista_cap[i]

def inverti_chiave_valore(dizionario):
    chiavi = list(dizionario.values())
    valori = list(dizionario.keys())
    newdict = {}
    for i in range(len(chiavi)):
        newdict[chiavi[i]] = valori[i]
    return newdict

d_cap_naz = inverti_chiave_valore(d_naz_cap)

while True:
    capitale = input("Capitale: ").capitalize()
    if capitale == "Stop":
        break
    elif capitale in d_cap_naz:
        print(d_cap_naz[capitale])
    else:
        print("La capitale indicata non è presente nell'elenco o non è stata digitata correttamente")