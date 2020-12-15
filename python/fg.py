from numpy import random

def lotto_fg(szam):
    szam=random.randint(91)
    return szam

for i in range(5):
    print(f'{lotto_fg(i)}, ',end='')  # csak kiírva

sorba=[]
for i in range(5):   # listába téve és rendezve
    sorba.append(lotto_fg(i))
sorba.sort()
print(sorba)


def fugv(a,b): # összead és 2X
    c=(a+b)*2
    return c

a=int(input('első szám: '))
b=int(input('második szám: '))
print(fugv(a,b))  # fg hívása