import logging
logging.basicConfig(filename="basic.log",level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

def Addition(x,y):
    return x+y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x/y

num1 = 20
num2 = 5

add = Addition(num1,num2)
logging.info(f"Addition of {num1} + {num2} = {add}")

sub = subtract(num1,num2)
logging.info(f"subtraction of {num1} - {num2} = {sub}")

mul = multiply(num1,num2)
logging.info(f"Multiplication of {num1} * {num2} = {mul}")

div = divide(num1,num2)
logging.info(f"Division of {num1} / {num2} = {mul}")


