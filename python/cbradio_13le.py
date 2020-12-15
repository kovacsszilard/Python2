from typing import List
from cb_osztaly import CBadas # from fájl neve, import osztály neve

# Olvassa be a cb.txt állományban lévő adatokat és tárolja el egy olyan adatszerkezetben,
# ami a további feladatok megoldására alkalmas! Az állományban legfeljebb 500 sor lehet. 
cb: List[CBadas]=[]
with open('cb.txt', 'r', encoding='UTF-8') as file:
    for sor in file.read().splitlines()[1:]:
        cb.append(CBadas(sor))



# 3.Határozza meg és írja ki a képernyőre a minta szerint, hogy hány bejegyzés található a forrásállományban:
print(f'3. feladat: Bejegyzések száma: {len(cb)} db ')



# Hat meg Gyuri névvel hány bejegyzés van:
gyuri_db: int=0
for i in cb:
    if i.nev=='Gyuri':
        gyuri_db+=1
print(f'Gyuri névvel {gyuri_db} bejegyzés van.')



# Melyik sofőr csinált egy percen belül lgtöbb adást? Holtverseny esetén összes adat:
max_adas_db:int=cb[0].adas_db
for i in cb[1:]:
    if i.adas_db>max_adas_db:
        max_adas_db=i.adas_db
print(f'A legtöbb adás 1 percen belül: {max_adas_db}')

# mivel a holtversenyt is kezelni kell:
for i in cb:
    if (i.adas_db==max_adas_db):
        print(f'Óra: {i.ora}:{i.perc} Név: {i.nev} {i.adas_db} db  adás')
    



# 4. Döntse el és írja ki a minta szerint, hogy található-e a naplóban olyan
# bejegyzés, amely szerint a sofőr egy percen belül pontosan 4 adást indított! A keresést ne
# folytassa, ha az eredményt meg tudja határozni:
volt_4:bool=False
for i in cb:
    if i.adas_db==4:
        volt_4=True
        break
if volt_4==True:
    print(f'4.feladat: Volt 4 adást indító sofőr (az első: {i.ora}:{i.perc} {i.nev} {i.adas_db} db)')
else:
    print('4.feladat: Nem volt 4 adás egy percben')




# 5. Kérje be a felhasználótól egy sofőr nevét, majd határozza meg a sofőr által indított hívások
# számát a napló bejegyzéseiből! Az eredményt a minta szerint írja ki a képernyőre! Ha olyan
# sofőr nevét adja meg a felhasználó, aki nem szerepel a naplóban, akkor a „Nincs ilyen nevű
# sofőr!” mondat jelenjen meg:
darab: int=0
neve=str(input('5.feladat: Kérem a sofőr nevét: '))
for i in cb:
    if i.nev==neve:
        darab+=i.adas_db

if darab>0:
    print(f'{neve} {darab}X használta a rádiót')
else:
    print('Nincs ilyen nevű sofőr')



# 6.Készítsen AtszamolPercre azonosítóval egész típusú értékkel visszatérő metódust vagy
# függvényt, ami a paraméterként megadott óra- és percértéket percekre számolja át! Egy óra
# 60 percből áll. Például: 8 óra 5 perc esetén a visszatérési érték: 485 (perc):

""" def AtszamolPercre(ora:int, perc:int)->int:
    atszamolva: int=(ora*60)+perc
    return atszamolva                       <- így is lehet, vagy az osztályba tenni a fg-t
 """    



# 7. Készítsen szöveges állományt cb2.txt néven, melybe a forrásállományban található
# bejegyzéseket írja ki új formátumban! Az órákat és a perceket percekre számolja át az előző
# feladatban elkészített metódus (függvény) hívásával! Az új állomány első sorát és
# az adatsorokat a minta szerint alakítsa ki:
try:
    with open('cb2.txt','w',encoding='UTF-8') as file:
        file.write('Kezdés,név,adás_db\n')
        for i in cb:
            file.write(f'{i.atszamolpercre()};{i.nev};{i.adas_db}\n')   # \n soremelés        
except:
    print('Hiba! Az írás nem sikerült!')

        

# 8. Határozza meg és írja ki a minta szerint a sofőrök számát a forrásállományban található
# becenevek alapján! Feltételezheti, hogy nincs két azonos becenév:
sofor_db: int=0
nevek: List=[]
for i in cb:
    if i.nev  not in nevek:
        nevek.append(i.nev)
        sofor_db+=1

print(f'8.feladat: Sofőrök száma: {sofor_db}')

# Ha ki akarjuk írni a nevüket:
# for i in nevek:
#     print(i)



# 9. Határozza meg a legtöbb adást indító sofőr nevét! A sofőr neve és az általa indított hívások
# száma a minta szerint jelenen meg:
db_lista: List[str]=[]
soforok: List[str]=[]
for i in cb:
    if i.nev not in soforok:
        soforok.append(i.nev)           # minden név csak egyszer szerepel már a listában

for i in soforok:
    adas:int=0
    for j in cb:
        if i==j.nev:            # belső ciklus ha i(sofő neve)=a cb lista névvel
            adas += j.adas_db   # akkor öszeadja az adások darabszámát
    
    db_lista.append(adas)       # ahány név annyi adás db kerül a listába

legtobb:int=0
for i, e in enumerate(db_lista):    # a litában lévő legtöbb adás szám indexe megkeresése
    if e>db_lista[legtobb]:
        legtobb=i

print('9.feladat: A legtöbb adást indító sofőr:')
print(f'\tNév: {soforok[legtobb]}')                     # A legtöbb adás indexe = a legtöbb adást indítő
print(f'\tAdások száma: {db_lista[legtobb]} alkalom')   # sofőr neve indexével