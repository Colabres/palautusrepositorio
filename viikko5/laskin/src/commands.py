class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.temp = 0    
        self.sovelluslogiikka= sovelluslogiikka
        self.lue_syote=lue_syote

    def suorita(self):
        self.temp = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.plus(self.lue_syote())

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.temp)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.temp = 0    
        self.sovelluslogiikka= sovelluslogiikka
        self.lue_syote=lue_syote

    def suorita(self):
        self.temp = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.miinus(self.lue_syote())        
        


    def kumoa(self):
        self.sovelluslogiikka.asettaarvo(self.temp)
    
               
class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.temp = 0
        self.sovelluslogiikka= sovelluslogiikka       
                



    def suorita(self):
        self.temp = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.nollaa()       

    def kumoa(self):
        self.sovelluslogiikka.asettaarvo(self.temp)

class Kumoa:
    def __init__(self, sovelluslogiikka,lue_komentoolio):
        self.komentoolio = lue_komentoolio
        
        self.sovelluslogiikka= sovelluslogiikka

    def suorita(self):

        self.komentoolio.kumoa()

  








