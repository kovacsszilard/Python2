#logikai operátorok
szam1=5
szam2=7

print (szam1 < szam2 and szam1==5) #mindegyik igaz => igaz

print (szam1 > szam2 and szam1 ==5) #második hamis => hamis

#vagy elég ha egy igaz:

print (szam1 > szam2 or szam1 ==5)

print (szam1 > szam2 and not szam1 ==5) # tagadás nem egyenlő 5-el