from numpy import random
from typing import List
import math

# 1.tölts föl egy listát 1-9999 10 db között véletlen számokkal:

lista: List[int]=[]     # while
while len(lista)<10:
    lista.append(random.randint(1,10000))
print(lista)

lista2: List[int]=[]    # for in
for i in range(10):
    lista2.append(random.randint(1,10000))
print(lista2)



# 2.határozzuk meg a 1,2,3,4 jegyű számok darabszámát:
# készíts a feladathoz a jegyek száma :int saját függvényt:

def jegyek_szama(lista):    # a függvény
    db_egyjegyu: int=0
    db_ketjegyu: int=0
    db_haromjegyu: int=0
    db_negyjegyu: int=0
    for i in range(len(lista)):
         if  lista[i]<10:
             db_egyjegyu+=1    
   
         if lista[i]>9 and lista[i]<100:
             db_ketjegyu+=1
            
    
         if lista[i]>99 and lista[i]<1000:
             db_haromjegyu+=1

         if lista[i]>999:
             db_negyjegyu+=1
    
    return db_egyjegyu,db_ketjegyu,db_haromjegyu,db_negyjegyu


# fg hívása:
for i in range(len(jegyek_szama(lista))):
    print(f'{i+1} jegyűek száma: {jegyek_szama(lista)[i]}')



print()
# 3.hat meg a 7 el osztható számok átlagát
# készíts a feladathoz 7 el osztahtó saját fg-t:

def hettel_oszthatok(lista):    # a függvény
    oszthato_hettel:int=0
    oszthato_het_db:int=0
    for i in range(len(lista)):
         if lista[i]%7==0:
             oszthato_hettel+=lista[i]
             oszthato_het_db+=1
    return oszthato_hettel,oszthato_het_db

print(f'Héttel oszthatók összege: {hettel_oszthatok(lista)[0]}')    # a fg hívása
print(f'darabszáma: {hettel_oszthatok(lista)[1]}')

if (hettel_oszthatok(lista)[0]) > 0:
    print('Héttel oszthatók átlaga: ',hettel_oszthatok(lista)[0]/hettel_oszthatok(lista)[1])
else:
    print('Nincs a listában 7-el osztható')



# 4.döntsd el, h található e a listában prím szám:

def prime(szam:int)->bool:                  # a függvény
    if szam>2 and szam%2==0 or szam==1:
        return False
    
    szam_gyoke: int=int(math.sqrt(szam))
    for oszto in range(3, szam_gyoke + 1, 2):
        if szam % oszto==0:
            return False
    return True

print('Prímszámok a listában:')
db=0
for i in range(len(lista)):
    segedvaltozo: int=0
    if prime(lista[i]):
        segedvaltozo=(lista[i])
        break
if segedvaltozo>0:
     print(f'Van prím szám a listában. Az első prím: {lista[i]}')
else:
    print('Nincs prím szám a listában')



# 5. Határozd meg a legnagyobb 3 jegyű szám indexét és értékét:

maxi: int = 0
legnagyobb3j=0
for i, e in enumerate(lista[1:]):

        #  if e >= lista[i] and (len(str(lista[i])))>2 and (len(str(lista[i])))<4:    # / így is lehet

         if e >= lista[i] and lista[i]<1000 and lista[i]>99:
             maxi = i            
             legnagyobb3j=(lista[maxi])

if legnagyobb3j>0:
    print(f'A legnagyobb 3 jegyű szám értéke: {legnagyobb3j}')
    print(f'A legnagyobb 3 jegyű szám indexe: {maxi}')
else:
    (print('Nincs 3 jegyű szám a listában'))