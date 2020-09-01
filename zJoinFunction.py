lis =["Virat","Dhoni","Rahul","Rohit","Bumbrah","Jadeja","Hardik"]

for item in lis:
    print(item,"and",end=" ")
print("Other Players")

#Instead
a = " and ".join(lis)
print(a)