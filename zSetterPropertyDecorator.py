class Employee:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname =lname

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @email.setter
    def email(self, email):
        name = email.split("@")[0]
        self.fname, self.lname = name.split(".")
    @fullname.setter
    def fullname(self,name):
        self.fname, self.lname = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Deleted...")
        self.fname = None
        self.lname = None



emp1 = Employee("jeevan", "gowda")

emp1.email = "gokul.gowda@gmail.com"

print(emp1.fname)
print(emp1.fullname)
print(emp1.email)

emp1.fullname = "manoj prince"

del emp1.fullname

print(emp1.fullname)
