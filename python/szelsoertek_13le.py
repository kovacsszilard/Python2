# A legnagyobb elem:
from typing import List
szamok: List[int]=(1,2,3,4,99,5,6,7,99)
max: int=szamok[0]
for i in szamok[1:]:
    if i>max:
        max=i
print(f'A legnagyobb elem: {max}')


# legnagyobb elem értéke és indexe range-el:
max_i:int=0
for i in range(1, len(szamok)):
    if szamok[i]>szamok[max_i]:
        max_i=i
print(f'A legnagyobb elem értéke: {szamok[max_i]}')
print(f'A legnagyobb elem indexe: {max_i}')


# legnagyobb elem értéke és indexe enumerate-val:
max_i2:int=0
for i, e in enumerate(szamok[1:]):
    if e>szamok[max_i2]:
        max_i2=i

print(f'A legnagyobb elem értéke: {szamok[max_i]}')
print(f'A legnagyobb elem indexe: {max_i}')


# több max érték esetén az összes elem indexe:
for i in range(len(szamok)):
    if szamok[i]==szamok[max_i]:
        print(f'{i};',end='')


# nem nevezhető ki az első elem legnagyobbnak/legkisebbnek:
min_i_paros:int=-1
for i in range(len(szamok)):
    if szamok[i]%2==0:  # ha az elem páros
        if min_i_paros== -1: # ha ez az első páros
            min_i_paros=i
        else:
            if szamok[i]<szamok[min_i_paros]:
                min_i_paros=i
if min_i_paros==-1:
    print('Nics páros szám')
else:
    print(f'A legnagyobb páros elem értéke: {szamok[min_i_paros]}')
    print(f'A legkisebb páros elem indexe: {min_i_paros}')