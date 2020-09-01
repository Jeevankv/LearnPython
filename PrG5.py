#Dictionary and its Function
d0 ={}
print(type(d0))
d1={
    "Jeevan":"Rcb",
    "Gokul":"Csk",
    "Mithun":"srh"
}
print(d1)
#Accessing
print(d1["Gokul"])
print(d1.get("Jeevan"))
#Changing value
d1["Mithun"]="kkr"
print(d1)
#Adding New Key VALue
d1["Manoj"]="Mi"
d1.update({"abhay":"kx1p"})
print(d1)
#Deleting Key
del d1["Manoj"]
d1.pop("abhay")
print(d1)

# Copy dictionary
d2=d1.copy()
print(d2)
del d1["Mithun"]
#or
d3=dict(d2)
print(d3)

#Functions
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

print(d1.keys())
print(d2.items())
#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

Myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print(Myfamily)