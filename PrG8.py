#FOR Loop and while loop
List=[10,"Jeevan",20,"gokul",5,7,2,9,12,1,34]
for x in List:
    if str(x).isnumeric() and x>=6:
        print(x)
for y in range(6):#range function
    print(y)

i=0;

while(i<5):
    print(i)
    i=i+1
#Brake
k=0
while(True):
    print(k)
    if (k==6):
        break
    k=k+1

z=0
while(z<12):

    z = z + 1
    if z==7 or z==9:
        continue
    print(z)

