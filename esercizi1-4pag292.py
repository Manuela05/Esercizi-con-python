'''Creare una classe Atleta per rappresentare le informazioni su un giocatore. La classe deve contenere un attributo booleano chiamato
visitaMedica aggiungere un metodo per assegnare il nome della squadra, uno chiamato effettua_visita che ponga visitaMedica uguale a True, uno
per visualizzare i dati del giocatore.'''

class Atleta:
    def visitaMedica(self, visitaMedica):
        self.visitaMedica = visitaMedica
    def squadra(self, squadra):
        self.squadra = squadra
    def effettua_visita(self):
        self.visitaMedica = True
    def info(self):
        if self.visitaMedica == True:
            print("L'atleta deve sottoporsi alla visita medica")
        print("Squadra dell'atleta:", self.squadra)
        