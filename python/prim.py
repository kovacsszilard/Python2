import math
def prime(szam:int)->bool:                  #  A függvény
    if szam>2 and szam%2==0 or szam==1:         # Ha a szám nagyobb mint 2 és páros vagy 1
        return False                            # akkor false, nem prím
    
    szam_gyoke: int=int(math.sqrt(szam))
    for oszto in range(3, szam_gyoke + 1, 2):   # Ha találunk osztót a szám gyöke előtt akkor sem prím
        if szam % oszto==0:
            return False
    return True


n: int=int(input("szám: "))     # szám bekérése
if prime(n):
     print("A szám prím")       # ha true a prime fg
else:
    print("A szám nem prim")    # else nem prím


# Prím számok keresése:
print("Prím számokat mitől meddig kéred?")
mitol: int=int(input("mitől: "))
meddig: int=int(input("meddig: "))

print(f'Prímszámok {mitol} és {meddig} között:')
db=0
for i in range(mitol, meddig):
    if prime(i):
        print(i,', ', end='')
        db+=1
print()               
print(f'A prímszámok {mitol} és {meddig} között: {db} db.')