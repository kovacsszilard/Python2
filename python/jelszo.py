jelszo = 'macska'

bemenet = input('jelszó: ')

proba=0

while bemenet != jelszo:
    proba +=1
    if proba==3:
        print('nincs több próba!')
        break
    print('nem jó')
    bemenet = input('jelszó: ')

if bemenet==jelszo:
    print('jó a jelszó')