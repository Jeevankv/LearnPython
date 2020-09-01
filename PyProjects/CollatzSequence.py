print("Enter the number")
try:
    n=int(input())
except ValueError:
    print("Enter valid integer")

def collatz(number):
        if number%2 == 0:
            number=number//2
            print(number)
            return number

        elif number%2 == 1:
            number= 3*number+1
            print(number)
            return number

while n!=1:
    n=collatz(n)















