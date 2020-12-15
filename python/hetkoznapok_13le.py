from typing import List
hétköznapok: List[str]=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

def magánhangzók(nap: str)->int:
    db=0
    for i in nap:
        if i in 'aáeéiíoóöőuúüű':
            db+=1
    return db

legtöbb=0
for i in range(len(hétköznapok)):
    if magánhangzók(hétköznapok[i])>magánhangzók(hétköznapok[legtöbb]):
        legtöbb=i

print(f'A legtöbb magánhangzó a {hétköznapok[legtöbb]} -ben van')