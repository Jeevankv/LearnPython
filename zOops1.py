class Student:
    """ doc type of this class"""
    college = "JSSATE"

    def __init__(self,name,usn,gender):#Constructor
        self.name = name
        self.usn = usn
        self.gender = gender

    def introduce(self):
        print(f"My Name is {self.name}")
        print(f"Usn : {self.usn}")
        print(f"Gender = {self.gender}\n")

    @classmethod
    def change_clgName(cls,newClg):
        cls.college = newClg

    @staticmethod
    def location(loc):
        print("{}".format(loc))



jeevan = Student("Jeevan","1JS18IS039","Male")
manoj = Student("Manoj","1JS18IS048","Male")

jeevan.introduce()

Student.introduce(manoj)


print(Student.__dict__)
print(Student.__doc__)
print(jeevan.__dict__)
print(jeevan.college)
# jeevan.college = "IIT Madras" #""" It creates a instance variable of college for jeevan Object """
# print(jeevan.college)

print(Student.college) #changing class variable using object does not change

#classMethod

print(jeevan.college)
Student.change_clgName("MIT")
print(jeevan.college)
print(Student.college)
print(manoj.college)
Student.location("Bangalore")#static method call

