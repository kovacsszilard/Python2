file=open('mese.txt','r',encoding='utf-8')

for sor in file:
    print(sor.strip())  # strip hogy le legyen sorköz


# while-al:


sor=file.readline()
while sor:
    print (sor.strip())
    sor=file.readline()