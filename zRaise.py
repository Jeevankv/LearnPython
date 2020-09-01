
# name = input("Enter you name")
# if not name.isalpha():
#     raise ValueError("Entered value should be a letter")
#
# print(f"Hello {name}")



try:
    a = input("Enter your name")
    b = int(input("Enter your Age"))


except Exception as e:
    print(e)
    if a == 'jeevan':
        raise ValueError("Jeevan has blocked")

    print("Exception Handled")

