vegyes=['macska', 'Tik',21,'malac','Vaddisznó',2.21,True]

for index, item in enumerate(vegyes):   # enumerate az indexet és az elemet adja vissza
    print(index, item)


print(hex(155)) # hexa-ba konvertál

print(len(vegyes)) #lista hossza

szoveg=('Sárga cica barna cica') # string hossza is
print(len(szoveg))

szamok=[3,4,2,34,55,2]
print(max(szamok))
print(min(szamok))

print(pow(10,2)) # hatványozás 
print(10**2) # ua.

print (list(range(0,100,10))) # mitől meddig, hányasával. listává alakítva

print(round(12.27)) # kerekítés
print(round(12.27234, 2)) # kerekítés hány számjegy legyen

print(sum(szamok))