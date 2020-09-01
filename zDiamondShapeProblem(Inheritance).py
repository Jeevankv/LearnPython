class A:
    def method(self):
        print("Methos of class A")
class B(A):
    def method(self):
        print("Methos of class B")
class C(A):
    def method(self):
        print("Methos of class C")
class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

print(d.method())

