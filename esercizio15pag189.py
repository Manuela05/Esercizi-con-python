'''Creare 2 liste contenenti l'una delle nazioni e l'altra le capitali corrispondenti con il medesimo indice; dopo aver chiesto una nazione
all'utente restituirne la capitale. Segnalare se la nazione non è presente nell'elenco'''

lista_naz = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaigian","Belgio", "Bielorussia","Bosnia ed Erzegovina", "Bulgaria","Cipro",
             "Croazia", "Danimarca", "Eire","Estonia", "Finlandia","Francia", "Germnania","Grecia","Islanda", "Italia","Kazakistan"]
lista_cap = ["Tirana", "Andorra la Vella", "Erevan", "Vienna", "Baku","Bruxelles", "Minsk","Sarajevo", "Sofia","Nicosia", "Zagabria",
             "Copenaghen", "Dublino","Tallinn", "Helsinki","Parigi", "Berlino", "Atene", "Reykjavik", "Roma","Nur-Sultan"]

nazione = input("Nazione: ").capitalize()

if nazione in lista_naz:
    print(lista_cap[lista_naz.index(nazione)])
else:
    print("Spiacente ma la nazione indicata non è presente nell'elenco ")