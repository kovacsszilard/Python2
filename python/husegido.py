import os
kilepes=''
while (kilepes==''):
    os.system('cls')
    print("Kiszámítom hány hónapra éri meg a hűségidő vállalása\n")    
    h=input('Ár hűségidővel: ')
    hn=input('Ár hűségidő nélkül: ')
    husegido=input('Hány év hűségidő (1 vagy 2) ? /alapértelmezett 1/:  ')
    print()
    h_int=int(h)
    hn_int=int(hn)
    hi=12
    nyereseg=""

    if (husegido=="2"):hi=24
    for i in range(hi):
         honapok_h=(h_int*(i+1))
         honapok_hn=(hn_int*(i+1))
         lemondas=( (hi-(i+1))*h_int   )
         veszteseg=(lemondas-(honapok_hn-honapok_h))
         if (veszteseg<1):nyereseg=("nincs veszteség!")
         print (i+1,"hó-ig hűségidővel:",honapok_h,"hűségidő nélkül:",honapok_hn,"lemondáskor fizetendő:",lemondas,"veszteség:",veszteseg,nyereseg)
    kilepes=input('\nKilépés: K + [enter]      Új számítás:[enter] ')