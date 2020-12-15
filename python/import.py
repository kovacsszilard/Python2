import math # az egész importálása
from math import pi # csak a pi-t importálja


print(math.pi)
print(math.sqrt(9))

# saját modul importálása:

import my_modul

my_modul.my_fg()    # meghívja a my_modul-ból a my_fg-t

import my_modul as macska   # lehet alias-t is adni

macska.my_fg()