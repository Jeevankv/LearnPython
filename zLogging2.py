import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


# Advance Logging

logger = logging.getLogger(__name__)
"""Now we have to use logger variable for logging statements"""
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(message)s:%(asctime)s')

file_handler = logging.FileHandler("employee.log")

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)




# logging.basicConfig(filename='employee.log', level=logging.DEBUG,
#                     format='%(levelname)s:%(message)s:%(asctime)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jeevan', 'Gowda')
emp_2 = Employee('Manjunath', 'Bhovi')
emp_3 = Employee('Abhay', 'Payadi')
emp_4 = Employee('Manoj', 'GH')