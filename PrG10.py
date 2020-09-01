#Global and Local Variables

x=25
def func1():
    y=35
    global x # Global value can be modified using global keyword
    x=12
    print(x,y)

func1()

# l1=[]
# inp=int(input("Enter no of item in list"))
# print(f"Enter {inp} Integer")
# for i in range(inp):
#     l1.append(int(input()))
# print(l1)
# from functools import reduce
# result = reduce(lambda x,y:x+y,l1)
# print(result)