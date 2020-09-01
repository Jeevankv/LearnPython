#MAP
l1 = ['32','13','24']
num=list(map(int,l1))
num[2]=num[2]+1
print(num)

l2 = [2,3,5,8,12,4]
sq =tuple(map(lambda x:x*x,l2))
print(sq)

def square(a):
    return a*a
def cube(a):
    return a*a*a

func_List = [square,cube]
for i in range(5):
    result= list(map(lambda x:x(i),func_List))
    print(result)

#Filter

l3 = [2,4,7,76,87,34,24,17,37,5]
ans = list(filter(lambda x:x<20,l3))
print(ans)

#Reduce
#reduce is function of Module functools
import functools
l4 =[1,2,3,4,5,6,7,8,9,10]
sum=functools.reduce(lambda x,y:x+y,l4)
print(sum)

