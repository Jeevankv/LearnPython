f1 = open("file1.txt")
try:
    with open("file.txt") as f:
        pass
except Exception as e:
    print("File Doesnt exist",e)
else:
    print("if except doesnt runs then else clause will run otherwise else will not run")

finally:
    print("Finally block runs compuslory,Used for code clean up")
    f1.close()


