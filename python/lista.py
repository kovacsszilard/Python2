# listák (módosítható)

lista=[]

print (lista) # még üres

lista.append(1)
lista.append(2)
lista.append(3)

lista.append('macska') # string is lehet

print (lista)

lista.remove('macska') # törlés a listából

print (lista)

lista.clear() #minden törése

print (lista)



# listába beszúrás:

lista.append(1)
lista.append(2)
lista.append(3)
print (lista)

lista.insert(2, 'tik') # hányadik pozícióba, mit
print (lista)

lista.reverse() #lista megfordítása
print (lista)


#sorba rendezés:
lista2=[12,2,34,0,72,53,44,1]
lista2.sort()
print (lista2)

lista3=['vizilú','tik','macska','tehén','alma',]
lista3.sort() # string sorbarendezés abc szerint
print (lista3)

print (len(lista3)) #lista hossza

print (lista3[2]) #lista hanyadik eleme

print (lista3[1:4]) # szeletelés, a megadott indextöl a megadottig adja vissza (4 már nem)

print (lista3[1:]) # 1től végig



#többdimenziós listák:

lista_td=[[1,2,3],[4,5,6],[7,8,8]]
print (lista_td[1]) #  az index a belső listára mutat
print (lista_td[1][1]) # a belső listából hanyadik elem
print (lista_td[1][1:]) # a belső listából hanyadik elemtől


# range függvény:
tartomany=range(100)
print (tartomany)
print (list(tartomany)) # listává konvertálva