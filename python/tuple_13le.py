from typing import List

tuple1=('Tik','Tehén','Macska','Sünmalac')

tuple2=tuple((1,2)) # konstruktorral tuple-ból létrehozott tuple

print(tuple2)

tuple3=({'a','b','c'}) # konstruktorral halmazból

tuple4=(['a','b','c']) # konstruktorral listából létrehozott tuple


# Teljes tuple kiírása:
print (tuple1)

# egy elem kiírása:

print(tuple1[2])

#tartománnyal től-ig:

print(tuple1[1:3]) # a 3.index már nem

# tól - végig:

print(tuple1[1:])

# elejétől- ig:

print(tuple1[:2])

# negatív index /a 0-ik előtti az utolsó:

print(tuple1[-1])



#tuple for ciklussal:

for  i in tuple1:
    print(i,' ',end='')


print()
# for indexel:

for index, item in enumerate(tuple1):
    print(index, item)

    # print(f'tuple1[{index}]={item},end=''')


# Tartalmazás vizsgálat:

if 'Macska' in tuple1:
    print ('Van Macska a tuple-ban')    #nagybetű érzékeny
else:
    print('nincsen')


# tartalmazás vizsgálat bekéréssel:
szoveg=(input('Keresett szöveg a tupleban: '))
if szoveg in tuple1:
    print(f'Van {szoveg} a tuple-ban')
else:
    print(f'Nincs {szoveg} a tuple-ban')



#tuple hossza:
print(len(tuple1))

#tuple tölése:
del tuple2

# azonos értékű elemel db-száma:
tuple_db=(1,2,3,3,9,4,9)
print(tuple_db.count(9)) # 2 db 9 van a tuple-ban


# Megadott elem első előfordulásának az indexe:
print(tuple_db.index(1))


# tupla konvertlása listává:
lista1:  List[str]=list(tuple1) # ehez kell az import List
print(lista1)

lista1[1]='megváltoztatva'  # lista második eleme megváltoztatva lesz
print(lista1)


 #tuple megváltoztatása:
tuple1=tuple(lista1)
print(f'Ez már a felülírt tuple1: {tuple1}')


# Tuple-k összeadása:
tuple_a=('Tehén','Macska',)
tuple_b=(1,2)
tuple_c=tuple_a+tuple_b
print(tuple_c)