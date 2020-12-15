class Szemely:
    def __init__(self,veznev,kernev,kor,szin='barna'):
        self.veznev=veznev
        self.kernev=kernev
        self.kor=kor
        self.szin=szin


class Alkalmazott(Szemely):     # örökli a személy összes tulajdonságát
    vegettseg='tiketető'    # létre lehet hozni még tagváltozókat mik csak az Alkalmazottban vannak


valami=Alkalmazott('Kis','Malac',25)
print (valami.kernev)
print (valami.vegettseg)