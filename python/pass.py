""" while true:
    pass    nem csinál semmit """

for i in range(10):
    print (i)
    if i==5:        
        break

szam=0
while True:
    print (szam)
    if szam==5:
        break
    szam+=1
 
for i in range(10):
     if i==5:
         continue # Az öt kimarad
     print(i)

print ('Páratlan számok:')

szamlalo=0      # kiírja 20-ig a páratlan számokat
while True:
    szamlalo+=1
    if szamlalo % 2 == 0:
        continue
    print (szamlalo)
    if szamlalo>20:
        break

print ('Páros számok:')

szamlalo=0      # kiírja 20-ig a páratlan számokat
while True:
    szamlalo+=1
    if szamlalo % 2 != 0:
        continue
    print (szamlalo)
    if szamlalo>20:
        break