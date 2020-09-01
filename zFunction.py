# Functions and DocType
a=10
b=20
c=sum((a,b))
print(c)

def function1():
    print("its function1")
print(function1())
function1()

def Average(a,b):
    """This function is to calculate the average of the two numbers"""
    average= (a+b)/2
    return average
print(Average.__doc__)
x= int(Average(a,b))
print("Average is ",x)
