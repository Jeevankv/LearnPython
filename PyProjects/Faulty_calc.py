# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# operator=input()
#
#
# if a==45 and b==3 and operator=='*':
#     print("555")
# elif a==56 and b==9 and operator=='+':
#     print("77")
# elif a==56 and b==6 and operator=='/':
#     print("4")
# elif operator=='+':
#     print(a+b)
# elif operator=='-':
#     print(a-b)
# elif operator=='*':
#     print(a*b)
# else:
#     print(a/b)

##  cmd Utility
import argparse
import sys

def faulty(args):


    if args.x==45 and args.y==3 and args.o =='mul':
        return ("555")
    elif args.x==56 and args.y==9 and args.o =='add':
        return ("77")
    elif args.x==56 and args.y==6 and args.o =='div':
        return ("4")
    elif args.o == 'add':
        return (args.x+args.y)
    elif args.o == 'sub':
        return (args.x-args.y)
    elif args.o == 'mul':
        return (args.x*args.y)
    elif args.o == 'div':
        return (args.x/args.y)
    else:
        return "something went wrong"


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Faulty Calculator",usage="Faulty Calculator")
    parser.add_argument('--x',type=float, default=1.0 )
    parser.add_argument('--y',type=float, default=1.0 )
    parser.add_argument('--o',type=str, default="add" )

    args = parser.parse_args()
    sys.stdout.write(str(faulty(args)))




