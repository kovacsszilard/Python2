#egyágú: if:
print('Szám abszolútértéke:')
x: int=int(input ('x='))
if x<0:
    x=x*-1  # behuzás=ident
print(f'Abszuloút érték:{x}')


#kétágú: if-else:
print('Páros Páratlan')
x: int=int(input ('x='))
if x%2==0:
    print('A szám páros')
else:
    print('A szám páratlan')


#többágú: if-elif-else:
print('Érdemjegyhez tartozó szöveges értékelés:')
jegy= int=int(input('Kérem a jegyet:'))
if jegy==1:
    print('egyes')
elif jegy==2:
    print('kettes')
elif jegy==3:
    print('hármas')
elif jegy==4:
    print('négyes')
elif jegy==5:
    print('ötös')
else:
    print('nincs ilyen jegy')