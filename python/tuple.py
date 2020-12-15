# tuple - nem módosítható

lista=[1,2,3]   # ez lista []

tupl=(2,4,5,5,4)    # ez tuple () nem módosítható   különbség a zárójel

# tupl.append(5)  # ez hiba lesz

lista.append(9)

print(lista)

# átalakítani lehet:

tupl2=tuple(lista)  # listából tuple

print(tupl2)

lista2=list(tupl)   # tuple-ból lista

print(lista2)


print(tupl.index(2))    # adott elem indexe
print(tupl.count(4))    # adott elem db-száma