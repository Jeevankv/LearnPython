lang  = ["C","C++","Python","Java","JavaScript"]

# for i in lang:
#     print(i)
#
# else:  #  does not execute if for end with break keyword
#     print("For Loop  Traversed Properly")
#

# Use case

for i in lang:
    if i == "JavaScript":
        print("Found")
        break

else:print("Not Found ")