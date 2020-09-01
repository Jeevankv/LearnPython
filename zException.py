#Exception Handling

a=int(input("Enter A\n"))
b=int(input("Enter B\n"))

def Divide(a,b):
    try:
        c=a/b
        return c
    except Exception as e:
        print(e)

x = Divide(a, b)
print(x)










