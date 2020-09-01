#List and list function-- Mutable
sports = ["cricket","football","Basketball"]
print(sports)
sports.sort()
print(sports)
sports.reverse()
print(sports)
print(len(sports))
numbers=[10,20,30,40,50]
print(numbers[1:4:2])
print(numbers[::-1])
numbers.append(60)
print(numbers)
print(type(numbers))
sports.extend(numbers)
print(sports)
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
#Tuple -- Immutable

tp = (10,20,30)
print(tp)
print(type(tp))
tup=(1,) # single element - Comma required
#tup=(1) wrong its considers as normal variable not tupple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print(tp[1:3]) # tupple slicing
print(len(tp))
#can convert  tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Tuple Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#tuple methods

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
