# Lista rendezése Magyar abc szerint:

from typing import List

magyar_abc = "-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ" # Abc definiálása

lista: List[str]=['Ödön','Éva','Elek','Ádám','András','Aladár','Olga','Ámor','Amarant','Émile','Abigél','Őz','Őrs','Ökör']

abc_rendezve = sorted(lista, key = lambda word: [magyar_abc.index(c) for c in word])
 
for i in abc_rendezve:
    print (i,' ',end='')