#Decorators
#A decorator takes in a function, adds some functionality and returns it.

### Prog 1
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operate(func, x):
#     result = func(x)
#     return result
#
# a=operate(dec,19)
# print(a)

# a function can return another function.
# def is_called():
#     def is_returned():
#         print("Hello")
#
#     return is_returned
#
#
# new = is_called()
# new()

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(10,5)

### Prog 2
# def decor(fun):
#     def inner():
#         a=fun()
#         add = a+5
#         return add
#     return inner
#
# def decor2(fun):
#     def inner():
#         b=fun()
#         mul = b*5
#         return mul
#     return inner
# @decor
# @decor2
# def num():
#     return 10
# print(num())

### prog 3

def Html_tag(tag):
    def WrapText(txt):
        return "<{0}> {1} </{0}>".format(tag,txt)
    return WrapText

print_h1 = Html_tag("h1")
print(print_h1("Hello World"))

# def html(tag,txt):
#     return f"<{tag}> {txt} </{tag}>"

