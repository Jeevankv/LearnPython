class Student:
    """ doc type of this class Can be called read using Dunder Dict method"""
    college = "JSSATE"

    def __init__(self,name,usn,branch,marks):#Constructor
        self.name = name
        self.usn = usn
        self.branch = branch
        self.marks = marks

    def introduce(self):
        print(f"My Name is {self.name}")
        print(f"Usn : {self.usn}")
        print(f"Gender = {self.gender}\n")

    def __add__(self, other):
        return self.marks + other.marks
    def __repr__(self):
        return f"Student('{self.name}','{self.usn}','{self.branch}',{self.marks})"
    def __str__(self):
        return f"This the Object of Class Student"

jeevan = Student("Jeevan","1JS18IS039","ISE",35)
akshay = Student("Akshay","1JS18IS010","ISE",50)

print(jeevan+akshay)#Using Dunder __add__ to resolve this error

print(jeevan) #o/p:<__main__.Student object at 0x00000232C15C8400> Can Use Dunder repr and str methods

print(repr(jeevan))

# Order of execution is str and repr. when str method is not present then also if repr is there then it will execute that.
