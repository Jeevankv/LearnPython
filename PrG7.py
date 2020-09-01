# If Else and Elif
print("Enter the Age")
age=int(input())
if age<7 or age>150:
    print("wrong age")
elif age<18:
    print("Cannot Drive")
elif age==18:
    print("Cannot decide")
else:
    print("Can Drive")

#ShortHand If ,Else
a=int(input("Enter A"))
b=int(input("Enter B"))
if(a<b):print("A Lesser Than B")

print("A Lesser Than B") if(a<b) else print("B is Lesser Than A")