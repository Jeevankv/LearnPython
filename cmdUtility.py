import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "div":
         return args.x / args.y

    elif args.o == "sub":
        return args.x - args.y
    else:
        return "Something Went Wrong"



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Two Digit Calculator",usage="\nUsed to calculate two numbers Ex:add,mul,div,sub\n",
                                     description="\nError Occur because of Wrong syntax ,Becareful",
                                     epilog="\nUse argument as described in the Help section\n")
    parser.add_argument('--x', type=float, default = 1.0,
                        help="\n--x <value>")

    parser.add_argument('--y', type=float, default=3.0,
                        help="\n--y <value>")

    parser.add_argument('--o',type=str , default="add",
                        help="\n--o <operation>")

    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))



