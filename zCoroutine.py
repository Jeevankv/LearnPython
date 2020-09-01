def searcher():
    import time
    book = "Assuming this a Huge Book and want search words in this book"
    time.sleep(4) # Assuming that 4sec as the time required for doing task

    while True:
        text = yield
        if text in book:
            print("Text found in the book")
        else:
            print("Text not found in the book")


search = searcher()
# print(search)
search.__next__()
# or next(search)

search.send("Huge Book")
input()
search.send("this")
# search.__next__()
search.send("Hujkjkjkje")
search.close()