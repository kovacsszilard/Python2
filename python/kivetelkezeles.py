try:
    print(semmi)    # nem definiált változó
except NameError as e:
    print(e)


lista=[1,2,3]
try:
    print(lista[4])
except IndexError as e:
    print(e,'lista nem létező indexe')


try:
    print (1/0)
except ZeroDivisionError as e:
    print(e,'Nullával nem lehet osztani')


vegyes=['macska',9, 'Tik',21,'malac','Vaddisznó',2.21,77,True,]  # A True értéke 1 ezért 10-el megszorozza
for i in vegyes:
    try:
        print(int(i*10))        # vegyes listából a számokat megszorozza
    except:
        continue                # ha nem szám megy tovább


try:
    print(semmi)
except:
    print('Nem definiált változó')
else:
    print('Ez csak akkor ha except nem fut le')
finally:
    print('Mindig lefut')



print('Nem szakad meg a futás')