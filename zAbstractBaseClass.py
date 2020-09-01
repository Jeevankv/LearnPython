# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod
# class Shape(ABCMeta): This can also be used when ABCMeta is imported.
class Shape(ABC):
    @abstractmethod
    def printArea(self):
        pass

class Rectangle(Shape):
    sides = 4
    def __init__(self,l,b):
        self.lenght = l
        self.breadth = b
    def printArea(self):
        return self.lenght * self.breadth

class Triangle(Shape):
    sides = 3
    def __init__(self,b,h):
        self.breadth = b
        self.height = h

    def printArea(self):
        return 0.5 * self.height * self.breadth


R1 = Rectangle(20,40)
T1 = Triangle(25,50)
print(R1.printArea())
print(T1.printArea())

