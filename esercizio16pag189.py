'''Creare 2 liste contenenti l'una delle nazioni e l'altra le capitali corrispondenti nella medesima posizione; dopo aver chiesto una nazione
all'utente restituirne la capitale. Segnalare se la nazione non è presente nell'elenco'''

lista_naz = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaigian","Belgio", "Bielorussia","Bosnia ed Erzegovina", "Bulgaria","Cipro",
             "Croazia", "Danimarca", "Eire","Estonia", "Finlandia","Francia", "Germnania","Grecia","Islanda", "Italia","Kazakistan"]
lista_cap = ["Tirana", "Andorra la Vella", "Erevan", "Vienna", "Baku","Bruxelles", "Minsk","Sarajevo", "Sofia","Nicosia", "Zagabria",
             "Copenaghen", "Dublino","Tallinn", "Helsinki","Parigi", "Berlino", "Atene", "Reykjavik", "Roma","Nur-Sultan"]

d_naz_cap = {}
for i in range(len(lista_naz)):
    d_naz_cap[lista_naz[i]] = lista_cap[i]

while True:
    nazione = input("Nazione: ").capitalize()
    if nazione == "Stop":
        break
    elif nazione in d_naz_cap:
        print(d_naz_cap[nazione])
    else:
        print("Spiacente la nazione indicata non è presente nell'elenco")