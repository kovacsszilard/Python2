def Osszead(a: int, b:int)->int:     # visszatérési érték típusa    
    return a+b

#függvény használata: hívás

print(Osszead(5,2))


def lnko(a:int, b:int)->int:
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

#fg hívás:
x1: int=12
x2:int=8
print(f'lnko({x1},{x2})={lnko(x1,  x2)}')