from typing import List

class Épület:
    név: str    
    város: str
    ország: str
    magasság: float
    emelet: int
    épült: int

    def __init__(self, sor: str)-> None:
          név, város, ország, magasság, emelet, épült=sor.split(';')
          self.név=név          
          self.város=város
          self.ország=ország
          self.magasság=float(magasság.replace(',','.'))
          self.emelet=int(emelet)
          self.épült=int(épült)

def main()-> None:
    # 1. Olvassa be a legmagasabb.txt állományban lévő adatokat:
    épületek: List[Épület]=[]
    with open('legmagasabb.txt','r',encoding='UTF-8') as file:
        for sor in file.read().splitlines()[1:]:
            épületek.append(Épület(sor))   

   
    # 2. Határozza meg hány épület található az állományban:
    print(f'2. feladat: Épületek száma: {len(épületek)}')

   
    # 3. Határozza meg az épületek emeleteinek az összegét:
    összemelet: int=0
    for i in épületek:
        összemelet+=i.emelet    
    print(f'3. feladat: Emeletek összege: {összemelet}')


    # 4. Határozza meg a legmagasabb épületet:
    legmagasabb: Épület=épületek[0]
    for i in épületek[1:]:
        if i.magasság>legmagasabb.magasság:
            legmagasabb=i
    print(f'\tNév: {legmagasabb.név}')
    print(f'\tVáros: {legmagasabb.város}')
    print(f'\tOrszág: {legmagasabb.ország}')
    print(f'\tMagasság: {legmagasabb.magasság} m')
    print(f'\tEmeletek száma: {legmagasabb.emelet}')
    print(f'\tÉpítés éve: {legmagasabb.épült}')


    # 5. Döntse el, hogy az adatok között található-e olasz épület:
    van_e_olasz: bool=False
    for i in épületek:
        if i.ország =='Olaszország':
            van_e_olasz=True
            break
    print(f'5. feladat: {"Van" if van_e_olasz else "Nincs"} olasz épület az adatok között!')

    # 5.más megoldás:
    if van_e_olasz==True:
        print('5. feladat: van olaszország')
    else:
        print('5. feladat: nincs olaszország')


    # 6.Készítsen statisztikát országok szerint az épületek számáról:   /szótárral/
    szótár: dict[str,int]=dict()
    for i in épületek:
        if i.ország in szótár:
            szótár[i.ország]+=1
        else:
            szótár[i.ország]=1
    
    for key, value in szótár.items():
        print(f'\t{key} - {value} db')


if __name__ == "__main__":
        main()