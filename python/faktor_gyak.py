print('Faktoriális gyak függvénnyel')
n=0
def faktor(n):  # ez a függvény
    n: int=int(input('n= '))
    fakt=1
    for i in range(2,n+1):
        fakt=fakt*i
        print (f'{i} !={fakt}')
    


faktor(n)   # fg meghívása