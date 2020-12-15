kaja_ar={'krumpli':178,'dinnye':200,'kenyér':82}

for item in kaja_ar.keys():
    print(item)                  # kiírja a kulcsokat


for item in kaja_ar.values():
    print(item)

for key,value in kaja_ar.items(): 
    print(key, value)


kaja_ar['rizsa']=289    # szótárhoz új hozzáadása

print(kaja_ar)

kaja_ar.pop('rizsa')

print(kaja_ar)

print(kaja_ar.get('krumpli'))   # kulcs étéke