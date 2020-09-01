#Order of passing argument (normal,args,kwargs)
def fun1(*args):
    print(type(args))
    print(args)
List = ["Jeevan","Abhay","Manoj"]
fun1(*List)

d = dict(name ="Jeevan",branch ="ISE")
def fun2(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
fun2(**d)

def fun3( name = "Jeevan"):#Default parameter
    print(name)
fun3("Manoj")
fun3("Abhay")
fun3("akshay")
fun3()
fun3("Manju")