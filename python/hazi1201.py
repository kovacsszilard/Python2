import math
# 1.Kérjen be két egész valós számot a felhasználótól, írja ki melyik a nagyobb

a: int=int(input('a= '))
b: int=int(input('b= '))
if a>b:
    print('A nagyobb')
elif a<b:
    print('B nagyobb')
else:
    print('Egyenlőek')



# Kérje be egy 3szög oldalait és hat meg a 3szög megszerkeszthető e
# megszerkeszthető: ha bármely 2 oldalalának öszege nagyobb mint a harmadik

print('Add meg a háromszög oldalait:')
a: int=int(input('a= '))
b: int=int(input('b= '))
c: int=int(input('c= '))
try:
    if (a+b)>c and (a+c)>b and (b+c)>a:
        print('A háromszög megszerkeszthető')   # 5 6 7 
    else:
        print('Nem szerkeszthető meg')    # 2 3 6
except:
    print('Egyik oldal sem lehet 0 vagy kisebb !')



# kérje be egy 3szög oldalait és hat meg a ter és ker Heron képlettel:
# feltétlezheti h megszerkeszthető
# Heron képlet: s = K/2
# T = Gyök(s*(s-a)*(s-b)*(s-c))
# megoldás:

a: float=float(input('a= '))
b: float=float(input('b= '))
c: float=float(input('c= '))

kerulet: float= a+b*c
s: float=kerulet/2
terulet: float=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'K= {kerulet}')
print(f'T= {terulet}')



# 4. kérje be téglalap oldalait, ker és ter
#T=a*b
#K=2*(a+b)

print('Add meg a téglalap oldalait:')
a: int=int(input('a= '))
b: int=int(input('b= '))

print(f'A téglalap területe: {(a*b)}')
print(f'A téglalap kerülete: {(2*(a+b))}')



# 5. hat meg két egész szám legnagyobb közös osztóját:
# mindaddig kissebítse a nagyobbik számot a kisebbikkel amíg a 2 szám egyenlő nem lesz

print('LNKO:')
a: int=int(input('a= '))
b: int=int(input('b= '))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'LNKO= {a}')