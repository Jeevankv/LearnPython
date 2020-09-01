from functools import lru_cache
from time import sleep

i = int(input("Enter maxsize for lru_cache"))

@lru_cache(maxsize=i)  # maxsize is to tell how many least recently used data to be saved in cache
def add(a, b):
    sleep(5)
    return a + b


if __name__ == '__main__':
    while True:
        a = int(input("Enter A"))
        b = int(input("Enter B"))
        print(add(a, b))  # Stores recently called function value, if same is called again it return stored value.So
        # the sleep(5) doesnt execute if the function call was in stored cache
