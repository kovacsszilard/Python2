class Szemely:
    veznev=''
    kernev=''
    kor=''

    def set_kor(self,value):    # metódus osztályon belül van
        self.kor=value  # a self az objektumpédányra mutat

    def set_nev(self,value):
        self.kernev=value


sz1=Szemely()

sz1.set_kor(16)
sz1.set_nev('macska')

print(sz1.kor)
print(sz1.kernev)