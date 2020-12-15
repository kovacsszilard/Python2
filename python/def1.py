''' szamlista=(list(range(100)))

def szamkiir(szamok):   # def a függvény létrehozása
    for i in szamok:
        print(i)

szamkiir(szamlista)     # függvény meghívása
 '''

vegyes=['macska', 'Tik',21,'malac','Vaddisznó',2.21,True]

def kiir(kiirlista):    # függvény
    for elemek in kiirlista:
        if isinstance(elemek, str):     # ha az elem str típusu            
            print(elemek.upper())       # akkor nagybetüsen kiírja
        else:                           # különben
            print('nem string hanem: '+ str(type(elemek)))  # 'szöveg + stringé alakítva az elemek típusa

kiir(vegyes)    # függv meghívása