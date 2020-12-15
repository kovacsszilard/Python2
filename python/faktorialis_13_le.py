print("Faktoriális")
#5! = 1*2*3*4*5
n: int=int(input('n= '))
faktor: int=1
for i in range(2,n+1):
    faktor = faktor*i
print(f'{n}!={faktor}')




print('Faktoriális meghatározása függvénnyel 10-től 30-ig:')
for n in range(10,31):
    faktor: int=1
    for n in range(2,n+1):
        faktor=faktor*i
    print(f'n!={faktor}')