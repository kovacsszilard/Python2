from typing import List

# lista létrehozása:
lista1: List[str]=['Macska','Tik','Tehén']
lista2=list((1,2,3)) # konstruktorral tupl-ból létrehozva
lista3=({5,6,7}) # konstruktorral halmazból

# számsorozatból létrehozva:
# 1: kezdőérték 1 től
# 2: meddig 23-ig / ez a szám már a listában nem lesz
# 3: hányasával
lista4=list(range(1,23,1))
print(lista4)

# Hivatkozás lista elemére:
print(lista1[0])
# tartományra:
print(lista1[0:2])
# től végig:
print(lista1[1:])
# elejétől v.meddig:
print(lista1[:2])


# Értékadás:
lista4[0]='Valami'  # már definiált kell h legyen!
print(lista4)


# Lista bejárása index nélkül:
for i in lista4:
    print(i,end='')


print()


# Lista bejárása indexekkel:
for index, item in enumerate(lista4):
    print(f'lista4 {index}.eleme: {item}')


# Tartalmazásvizsgálat:
if 18 in lista4:
    print('Van 18 a listában')
else:
    print('nincs')



# lista hossza:
print(len(lista4))

# Elem hozzáadása a végéhez:
lista4.append(89)

# Elem beszúrása:
lista4.insert(3,77) # A megadott index(3) elé teszi (77)
print(lista4)   # elejére: 0


# Törlés a listából:

# Megadott nevű elem törlése:
lista4.remove('Valami')
print(lista4)


# Utolsó elem vagy a megadott indexű törlése:
lista4.pop()    # utolsó
print(lista4)

lista4.pop(2)
print(lista4)


# lista ürítése, miden elem törlődik:
lista4.clear()
print(lista4)

# lista törlése:
del lista4


# Lista másolása:
# nem készül tényleges másolat, ez csak referencia
# ua. memóriacímre mutat
lista7=lista1
print(lista7)

# copy()-val:
lista7=lista1.copy()

# másolat konstruktorral:
lista7=list(lista1)


# meghat értékű elemek darabszáma:
lista8=(0,1,2,3,2,4,2)
print(lista8.count(2)) # hány db. 2-es van a listába


# meghat értékű elem első előfordulásának indexe:
print(lista8.index(2))  # 2 lesz


# Lista bővítése másik listával: extend:
# az elsőhöz hozáfűzte a második listát
lista_egy=['krumpli','macska']
lista_ketto=[1,2]
lista_egy.extend(lista_ketto)
print(lista_egy)


# lista megfordítása:

lista9=list(range(1,10,1))
print(lista9)

lista9.reverse()    # megfordítás

print(lista9)


# lista rendezése:

lista0=[2,4,0,2,7,11,88,22] # növekvő
lista0.sort()
print(lista0)

lista0.sort(reverse=True)   # csökkenő
print(lista0)