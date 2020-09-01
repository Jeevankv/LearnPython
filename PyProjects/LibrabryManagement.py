class Library:
    dic = {}  # Class variable Which is used for storing Bookname(Key):Username(value) pair
    booklist = ["b1", "b2", "b3", "b4", "b5"]  # List contains the books

    def __init__(self, libname):

        self.libname = libname

    def displaybook(self):  # Used for displaying available books
        if len(self.booklist) == 0:  # used to check whether the list is empty or Not
            print("No Books are available")
        else:
            for books in self.booklist:  # Traversing through list and printing it
                print(books, end="\t")

    def lendbook(self):

        print("Enter your Name")
        name = input()
        print("Enter the Name Of the Book You Want To Lend")
        bookname = input()
        flag = 0  # Used for checking whether the book present in list or not
        for book in self.booklist:
            if book != bookname:  # check untill the book and the bookname is same
                continue  # if condition fails return back to for loop
            else:
                flag = 1  # If condition is true then flag is set to high
        if flag == 0:
            print("Book is not Availble")
            print("Book is available with : {}".format(self.dic.get(bookname)))  # using dictionary to show with whom
            # the book is available currently
        else:
            print("Book is available")
            print("Lent Successfully...")
            self.dic.update({bookname: name})  # Adding the book and the user to the dictionary
            self.booklist.remove(bookname)  # After Lent removing the book from the list

    def add(self):
        print("Name of the book you want to ADD")
        bookname = input().casefold()  # Adds the bookname to list ,automatically lowers the case of input
        self.booklist.append(bookname)  # Bookname is added to the list
        self.booklist.sort()  # list is sorted
        print("Thank You! for Your contribution")

    def returnbook(self):
        print("Enter Your name")
        name = input()
        self.booklist.append(list(self.dic.keys())[list(self.dic.values()).index(name)])  #   key is obtained by taking the value and added to the list
        self.booklist.sort()  #  list is sorted
        self.dic.pop(list(self.dic.keys())[list(self.dic.values()).index(name)])  # dictionary key-value are removed by providing key to the pop function
        print("Returned Successfully...")


if __name__ == '__main__':

    lib = Library("Jeevan Librabry")
    from sys import exit
    while True:
        print("\n1:Display\t2:Lend\t3:Add\t4:Return\t5:Exit\n")
        userinp = int(input("Enter Your Input\n"))
        if userinp == 1:
            lib.displaybook()
        elif userinp == 2:
            lib.lendbook()
        elif userinp == 3:
            lib.add()
        elif userinp == 4:
            lib.returnbook()
        elif userinp == 9:  # Just for seeing the dictionary elements for debugging
            print(lib.dic)
        else:
            exit()
