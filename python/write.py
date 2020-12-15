#'r' read
#'w' write
#'a' append / hozzáfűzés


with  open('írás.txt','w',encoding='utf-8') as file:
    szoveg='Malacgyerek'
    file.write(szoveg)                      # szöveg fájlba írás

file.close()

with open('mese.txt','r',encoding='utf-8') as infile:       # fájl beolvasása
    with open('mese2.txt','w',encoding='utf-8') as outfile: #  majd másik fájlba írása

        sor=infile.readline()   # beolvas egy sort

        while sor:
            outfile.write(sor)  # kiírja mese2.txt fájlba            
            sor=infile.readline() # beolvassa a következő sort


#append:

with open('írás.txt','a',encoding='utf-8') as file: # megnyit egy fájlt
    hozzafuzes="\nHozzáfűzött szöveg"                 # és a szöveget hozzáfűzi     \n  <-új sor
    file.write(hozzafuzes) 