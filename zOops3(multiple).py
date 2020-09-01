class Employee:
    Holidays = 15
    def __init__(self,Ename,EGender,Ephone):
        self.name =Ename
        self.gender = EGender
        self.phone = Ephone
    def printdetails(self):
        return f"Name: {self.name}\nGender: {self.gender}\nPhone: {self.phone}"

class Programmer:
    Holidays = 10
    def __init__(self,Ename,EGender,Ephone,language):
        self.name = Ename
        self.gender = EGender
        self.phone = Ephone
        self.language = language
    def printLanguage(self):
        return f"{self.language}"

class DataScientist(Employee,Programmer):#Multiple Inheritance
    ExtraSkills = ["ML","AI","DeepLearning","NLP"]

EMP1 = DataScientist("Jeevan","Male","9876543210")
# print(EMP1.printdetails())

EMP2 = Programmer("Akshay","Male","9846829192",["C","C++","Java","Python"])
print(EMP2.printLanguage())
EMP3 = DataScientist("Manoj","Male","9878789899")
print(EMP3.Holidays)
