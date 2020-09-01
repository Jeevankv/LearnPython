class Student:
    def __init__(self,name,usn,address):
        self.name = name
        self.usn = usn
        self.address = address

    def display(self):
        return f"Name: {self.name}, USN: {self.usn}, Address: {self.address}"

if __name__ == '__main__':
    import pickle
    with open("picking.dat","wb") as f:
        str1 = Student("jeevan", 39, "chikmagalur")
        pickle.dump(str1,f)
        print("pickling Done..")

    with open("picking.dat","rb") as f:
        obj = pickle.load(f)
        print("Unpickling Done..")
        print(obj.display())





