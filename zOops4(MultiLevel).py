class Dad:
    Basketball = 11
    cricket =2

class Son(Dad):
    Dance = 7
    guiter =20

class Grandson(Son):
    singer = 10
    keyboard =28
    Dance = 14

p1 = Dad()
p2 = Son()
p3 = Grandson()

print(p3.Basketball)
print(p3.singer)
print(p2.Basketball)
print(p3.Dance)
print(p3.cricket)