'''Elencare le proprietà  e i metodi della classe Prodotto. Definire il metodo assegna_prezzo.'''

class Prodotto:
    def __init__(self, categoria, prezzo, quantità):
        self.categoria = categoria
        self.prezzo = prezzo
        self.quantità = quantità

    def calcola_sconto(self, sconto):
        self.prezzo = round(self.prezzo - (self.prezzo/100*self.sconto))
        
    def calcola_tot(self):
        self.tot = self.prezzo*self.quantità
        
    def mostra_info(self):
        print("Prezzo:", self.prezzo)
        print("Quantità:", self.quantità)

carne = Prodotto("Alimento", 100, 2)
carne.mostra_info()
