class Car:
    """DocType"""
    no_of_seats = 4
    def __init__(self,name,price,Type):
        self.ModelName = name
        self.price = price
        self.Type = Type

    # prints the details like name,price,type
    def printDetails(self):
        return f"Name:{self.ModelName}\nPrice: {self.price}\nType:{self.Type} "


bmw = Car("BMW","1M$","sports")

print(type(bmw))
print(id(bmw))
print(dir(bmw)) # says what can done ti this object

from inspect import *

print(getmembers(bmw))

print(getattr(bmw,"no_of_seats"))
print(getmodule(bmw)) #Gives address of the source code

print(getdoc(bmw))
print(getcomments(bmw))