#Public
#protected
#private

class Employee:
    Public = 10
    _Protected = 20
    __Private = 30

emp1 = Employee()

print(emp1.Public)
print(emp1._Protected) # protected data can be accessed by the parent class and the derived class

#print(emp1.__Private) -> Error-AttributeError: 'Employee' object has no attribute '__Private' .Cannot be accessed directly becz of  "Name Mangaling"

print(emp1._Employee__Private) # We have write "_Class__Private_Attribute" to Access