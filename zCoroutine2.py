def print_name(lname):
    print("Searching prefix:{}".format(lname))
    try:
        while True:
            name = (yield)
            if lname in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("gowda")
corou.__next__()
corou.send("jeevan")
corou.send("jeevan gowda")
corou.close() 