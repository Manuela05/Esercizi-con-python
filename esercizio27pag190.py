'''Organizzare con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome della persona, il
programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente nella rubrica.'''

rubrica = {"Rosa": 9718312783, "Marco": 4519569924, "Luca": 4121846258, "Nicolò": 4917486932, "Maria": 153534282, "Francesca": 5492958787}

nome = input("Nome: ").capitalize()
if nome in rubrica:
    print(rubrica[nome])
else:
    print(nome, "non è nella rubrica")