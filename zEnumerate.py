# Enumerate() Function

L1 = ["jeevan","abhay","manoj","akshay","manju"]
S1="TheProgrammer"
obj1=enumerate(L1)
obj2=enumerate(S1)
for index,items in enumerate(L1):
    print(f"{index}--->{items}")

print()
for index,items in enumerate(S1):
    print(f"{index}--->{items}")