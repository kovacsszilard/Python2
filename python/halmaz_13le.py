from typing import Set

# Halmaz létrehozása elemekkel:
halmaz={'macska','kutya','tik'}
print(halmaz)

# inicializált típusos halmaz:
halmaz1: Set[str]={'macska','kutya','tik'}

# Egy elem hozzáadása:
halmaz.add('disznó')
print(halmaz)

# Több elem hozzáadása:
halmaz.update({'tehén','malac'})
print(halmaz)

# Elem törlése:
halmaz.discard('malac')

# Halmaz ürítése: clear()
# Halmaz teljes törlése: del

# Halmazok uniója: union()
h1={"a","b","c"}
h2={1,2,2}
print(h1.union(h2))

# Halmazok metszete:
h1={"a","b","c"}
h2={"d","e","c"}
print(h1.intersection(h2))

# Halmazok különbsége:
h1={"a","b","c"}
h2={"d","e","c"}
print(h1.difference(h2))