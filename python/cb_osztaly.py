class CBadas:   # osztály definíció
    ora:int
    perc:int    # adattagok
    adas_db:int
    nev:str
    # konstruktor fg:
    def __init__(self,sor:str)-> None:
        ora, perc, adas_db, nev= sor.split(';')
        self.ora=int(ora)
        self.perc=int(perc)
        self.adas_db=int(adas_db)
        self.nev=nev
    
    def atszamolpercre(self)->int:
     return self.ora * 60 + self.perc   # 6.feladat