
# def square(num):
#     for x in num:
#         yield x*x
#
# my_sqr = square([1,2,3,4,5])
#
# print(next(my_sqr))
# print(next(my_sqr))
# print(my_sqr.__next__())
# print(my_sqr.__next__())
#
# for x in my_sqr:
#     print(x)

def nextsquare():
    i =1
    while True:
        z = i*i
        yield z
        i+=1

for x in nextsquare():
    if x>100:
        break
    print(x)

    
