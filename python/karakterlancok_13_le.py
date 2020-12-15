from typing import List

a: str='Karakterláncok kezelése'
print(a)    # kiírja az egészet
print(a[1]) # kiírja az első karaktert
print(a[2:]) # másodiktól az egészet
print(a[2:9]) # másodiktól 9-ig karaktert

#string hossza:
print(len(a))


# Strint darabolása:
darabolt: List[str]=a.split('á') # á nem kerül bele
print(darabolt) # ahol 'á' van daabol


# Tartalmazás vizsgálat
print('macska' in a) # ha nincs bene akkor false
print('lánc' in a)


# String bejárása (karakterekként):
for i in a:
    print(i, end=' ')


print('KISBETŰS'.lower())   # kisbetűsé lesz
print('nagybetűs'.upper())   # nagybetűsé lesz
print(a.replace("a","x")) # csere

print(a.count('a')) # első előfordulás indexe