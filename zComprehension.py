

#  Normal method
# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)


#  List Comprehension

ls = [i for i in range(100) if i%3==0 ]
print(ls)

# Dictionary Comprehension

dic = { i:f"item{i}" for i in range(10)  if i%2==0 }
print(dic)

#  Reversing Key value Pair
dic1 = {value:key for key,value in dic.items()}
print(dic1)

#  set comprehension

set1 ={ car for car in ["BMW","Royce Rolls","Lamborghini","BMW","BMW"]+ ["BMW","ferrarri","Audi"]} # Set items does not repeat
print(set1)

#  Generator Comprehension

my_sqr = (sqr*sqr for sqr in [1,2,3,4,5] )
# print(my_sqr.__next__())
# print(my_sqr.__next__())
# print(my_sqr.__next__())
# print(my_sqr.__next__())
# print(my_sqr.__next__())
for i in my_sqr:
    print(i)