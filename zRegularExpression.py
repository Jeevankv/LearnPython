import re
## search Method

phoneregex = re.compile(r" [+]\d{2}-\d{10}")

match_object = phoneregex.search("the phone number is +91-9876543210")

print("My phone number is :", match_object.group())

##
#  Matching mutiple group with pipe

pattern = re.compile(r"batman|superman")
mo = pattern.search("I love both batman and superman")
print(mo.group()) # return first occurence of match if both represent in the match

## Matching optional
# ? character flag precedes group

patt  = re.compile(r"([+]\d{2})?[-]?\d{10}")  # if first group is present in string then gives it otherwise not.
mo = patt.search("My number is 9876543210")
mo1 = patt.search("My second number is +91-8976354232")
print(mo.group())
print(mo1.group())
print(mo1.groups())
country_code = mo1.group(1)
print(country_code)




