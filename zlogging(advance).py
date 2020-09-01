import logging
import zLogging2
"""  Now the logging configuration set to zlogging2's configuration, so the below logging 
                 configuration is not set to this file """

# logging.basicConfig(filename="basic.log",level=logging.INFO, # nothing gets added to basic.log everything gets added to employee.log
#                     format="%(asctime)s:%(levelname)s:%(message)s")  #  Not set because of import zlogging2

logger = logging.getLogger(__name__)
"""Now we have to use logger variable for logging statements"""
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler("basic.log")
file_handler.setLevel(logging.ERROR) # setting level to specified file
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()  # For displaying in console
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def Addition(x,y):
    return x+y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
       result = x/y
    except ZeroDivisionError:
        # logger.error("Tried to divide by zero")
        logger.exception("Tried to divide by zero")

    else:
        return result

num1 = 15
num2 = 0

add = Addition(num1,num2)
logger.debug(f"Addition of {num1} + {num2} = {add}")

sub = subtract(num1,num2)
logger.debug(f"subtraction of {num1} - {num2} = {sub}")

mul = multiply(num1,num2)
logger.debug(f"Multiplication of {num1} * {num2} = {mul}")

div = divide(num1,num2)
logger.debug(f"Division of {num1} / {num2} = {mul}")


