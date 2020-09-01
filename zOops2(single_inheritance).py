class Car:
    no_of_seats = 4
    def __init__(self,name,price,Type):
        self.ModelName = name
        self.price = price
        self.Type = Type

    def printDetails(self):
        return f"Name:{self.ModelName}\nPrice: {self.price}\nType:{self.Type} "


class RaceCar(Car):
    # super().no_of_seats
    no_of_seats = 2




BMW = Car("BMW","85,00,000","SUV")
details = BMW.printDetails()
print(details)

Lambo = RaceCar("Lamborgini","5,00,00,000","Sport")
print(Lambo.printDetails())
print(Lambo.no_of_seats)
print(BMW.no_of_seats)