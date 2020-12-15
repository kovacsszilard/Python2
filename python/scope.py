# FUNCTION SCOPE:

def test():
    a=5         # élettartam: A fg meghívásától a végrehajtásig
    print(a)

test()  # A fg létrehozz az a változót

# print(a)  <- itt már nem látszik az a változó csak a fg-ben.



# MODULE SCOPE:

a=78 # Az egész fájlon belül látható
print(a)

