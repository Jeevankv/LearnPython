import sys
print(sys.path)
import pandas
print(pandas.__version__)

#importing file from current directory
import zFunction  #importing py file runs everything written in that file
print(zFunction.Average(14, 18))

#importing py file runs everything written in that file
import zEnumerate

 # using "if __name__ == '__main__':"    can avoid this
# import time
# time.sleep(2)
# import os
# if os.name == 'posix':
#     _=os.system('clear')
# else:
#     _ = os.system('cls')

import time
a = time.time()
print(a)
time.sleep(5)
b=time.time()
print(b)
print(b-a)


