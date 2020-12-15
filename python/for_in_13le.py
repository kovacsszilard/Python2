print('3 jegyű páratlan számok összege')
osszeg1:int=0
for szam in range(100,1000):
    if szam % 2==1:
        osszeg1 += szam
print (f'{osszeg1=}') # kiírja az = miatt a váltoó nevt

# másik lehetőség:
osszeg2: int=0
for szam2 in range(101,1000,2):
    osszeg2+=szam2
print(f'{osszeg2=}')
    
