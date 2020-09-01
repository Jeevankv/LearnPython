import time
# print(time.time())
initial = time.time()
i=0

while i<=200:
    print("Hello World!")
    i=i+1
print("Time Taken to run while loop is ",time.time()-initial," Seconds")

initial2 = time.time()
for j in range(201):
    print("The Time")
print("Time Taken to Run For loop is ",time.time()-initial2,"Seconds ")


localTime = time.asctime(time.localtime(time.time()))
print(localTime)
print(time.localtime(time.time()))#returns as tuple
print(time.localtime())
print(time.asctime())
print(time.time())

#Sleep function
for i in range(5):
    print(i)
    time.sleep(2)