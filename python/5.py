""" from numpy import random
x=0
while  x != 100 :
    x=random.randint(101)   # eggyel nagyobbat kell mint amennyi kell
    print (x) """
import os   # ez a consol törléshez kell
kilepes=''
while kilepes=='':
    os.system('cls') #consol törlés
    i=0;x=0;lista=[]
    from numpy import random
    while i!=5:
      x=random.randint(91)
      if x>0:
        i+=1
        lista.append(x)

    print('Ötös lottó:')
    print('')

    lista.sort()
    for i in lista:
           print(i,', ',end = '')  # nem lesz új sor: end = ''

    print('')
    kilepes=input('\nKilépés: K + [enter]      Új számok:[enter] ')