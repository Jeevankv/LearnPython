
import re

# match zero or more with star

pattRegex = re.compile(r"colo(u)*r")
mo = pattRegex.search("My favorite colouuuuur is Blue")
mo1 = pattRegex.search("My favorite color is Blue")
print(mo.group())
print(mo1.group())

# # match onr or more with plus

ptregex = re.compile(r"bat(wo)+man")
mObj = ptregex.search("batwoman vs superman")
print(mObj.group())

pttrRegex = re.compile(r"bat(wo)+man")
mObj1 = pttrRegex.search("batman vs superman")
print(mObj1==None)


## Findall()

# pattern = re.compile(r"")



