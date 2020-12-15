a=5
b=10

def osszead1():
    print(a+b)      # nincs paramétere


def osszead2(a,b):
    return a+b      # visszatérési érték

def osszead3(*args):    # több is lehet
    return sum(args)



osszead1()

print (osszead2(20, 30))

osszeg=(osszead2(7,7)) # változóba mentve
print (osszeg)

osszeg3=osszead3(1,2,3,4)
print (osszeg3)



def szoveges(*args):
    szoveg='Ehez lesz hozzáfűzve'    
    for k in args:
        szoveg +=' , '
        szoveg +=k        

    print(szoveg)

szoveges('tik','macska','tehén','bogár')