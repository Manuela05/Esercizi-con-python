''''''

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
        