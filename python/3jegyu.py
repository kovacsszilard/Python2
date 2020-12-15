from numpy import random
from typing import List
import math

lista: List[int]=[]
while len(lista)<10:
    lista.append(random.randint(1,10000))
print(lista)
# 5. Határozd meg a legnagyobb 3 jegyű szám indexét és értékét:

lista_3: List[int]=[]   # ebbe kerülnek a 3 jegyű számok a listából
index=0

for i in range(len(lista)):
    if lista[i]  > 99 and  lista[i] < 1000:
        lista_3.append(lista[i])       # 3 jegyűek kiválogatása
lista_3.sort(reverse=True)             # hogy az első legyen a legnagyobb

if len(lista_3)>0:                 # ha van a listában valami:
    for i in range(len(lista)):
         if lista_3[0]==lista[i]:   # ha megyeggyezik a lista első eleme az indexel, akkor megvan az indexe
              index=i               # a legnagyobb 3 j. számnak
    
    print()
    print(f'A legnagyobb 3 jegyű szám a listában: {lista_3[0]}')
    print(f'A szám indexe: {index}')

else:
    print('Nincs a listában 3 jegyű szám')