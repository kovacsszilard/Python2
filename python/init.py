class Szemely:
    def __init__(self,veznev,kernev,kor,szin='barna'):
        self.veznev=veznev
        self.kernev=kernev
        self.kor=kor
        self.szin=szin

Cirmos=Szemely('Cirmos','Cica',2)   # Ha nem adunk meg többet akkor az alapértelmezett lesz (barna)
Macsk=Szemely('Macskaházy','Cicamér',4,'Tarka')

print(Cirmos.szin)
print(Macsk.szin)