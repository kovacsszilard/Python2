import random
from typing import List

# 1.1 Feltöltés felhasználói input útján:
""" nevek: List[str]=list()
input_db=int(input('Hány db név lesz? '))
input_nev: str=''

while input_db>0:
    input_nev=input('Kérem a nevet: ')
    if len(input_nev)>0:
        nevek.append(input_nev)
        input_db-=1

print(nevek) """


# 1.2 Feltöltés véletlen értékekkel:
szamok: List[int]=[]
for i in range(10):
    szamok.append(random.randint(0,91))

print(szamok)
"""
for i in szamok:
    print(i,',',end='')     # ha nem köll az index

print()

for i, j in enumerate(szamok):
    print(i,j)      # ha köll az index"""


# 1.4 Feltöltés szöveges állományból (sorokként csak egy adat van):
with open('bukk-videk.txt', 'r', encoding='UTF-8') as file:
    sorok:List[str]=file.read().splitlines()
magassagok: List[float]=[]
for i in sorok:
    magassagok.append(float(i))

print(magassagok[:14])  # csak eddig írj aki """

# Páros / páratlan fg-vel:
""" def paros_paratlan(szam)-> int:
    paros=True
    if szam%2==0:
        paros=True
    else:
        paros=False
    return paros


szam=int(input('Szám: '))

if(paros_paratlan(szam))==True:
    print('Páros')
else:
    print('Páratlan') """


# 3.2 Megszámlálás tétele, páratlan számok 500-ig:
""" paratlan_db=0
for i in range(501):
    if i%2 !=0:
        paratlan_db+=1

print(f'{paratlan_db} db. páratlan van 500-ig') """


# 3.3 Összegzés tétele páros számok öszeg 500-ig:
""" paros_ossz=0
for i in range(501):
    if i%2==0:
        paros_ossz+=i
print(f'A páros számok öszege 500-ig: {paros_ossz}')"""

# 3.4 Szélsőérték (minimum, maximum):
""" max: int=szamok[0]
for i in szamok[1:]:
    if i>max:
        max=i
print(f'A legnagyonn a listában: {max}')

min: int=szamok[0]
for i in szamok[1:]:
    if i<min:
        min=i
print(f'A legkisebb a listában: {min}') """

# Buborékrendezés:
for i in range(len(szamok) - 1, 0, -1):
    csere_volt:bool=False
    for j in range(i):
        if (szamok[j]>szamok[j+1]):
            sg_valtozo:int=szamok[j]
            szamok[j] = szamok[j+1]
            szamok[j+1]=sg_valtozo
            csere_volt=True
    if csere_volt is False:
        break
print(f'Számok rendezve: {szamok}')