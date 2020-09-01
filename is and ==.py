# == -> variable equality- Two object have same value
# is -> reference equality- reference refer to same object

a = [1,2,3]
b = [1,2,3]

print(a==b) # True because value are equal
print(a is b) # False ,because does not refer to same object

b = a
print(a==b) # True
print(b==a) # True

print(a is b) # True because both reference to same object
print(b is a) # True

c = a[:] # c is copy of a
print(c==a) # True
print(c==b) # True

print(c is a) # False Does not refers to same object


