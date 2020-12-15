import math
a=float(input('a= '))
b=float(input('a= '))
c=float(input('a= '))
if a!=0:
    if math.pow(b,2)>=4*a*c:
        if math.pow(b,2)>4*a*c:
            print('Két gyök')
            x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
            x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
            print(f'x1= {x1}')
            print(f'x2= {x2}')
        else:
            x=-b/(2*a)
    else:
        print('Nincs valós gyök')
else:
    print('Nem másodfokú')
    if b!=0:
        x=-b/c
        print(f'x= {x}')
    else:
        if c!=0:
            print('Ellentmonsás')
        else:
            print('Azonosság')