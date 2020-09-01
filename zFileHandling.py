# File Handling
# "r" - open file for reading - Default Mode
# "w" - Open a file for writing
# "x" - creates file if not exists
# "a" - Add more content to a file
# "t" - text mode - Default Mode
# "b" - binary mode
# "r+" - read and write

# #File read
#
# f=open("file.txt")
# # print(f.read())
# # print(f.read(5))
# # print(f.read(5))
# # print(f.read())
# #print(f.readline())
# print(f.readlines())
# # for line in f:
# #     print(line,end="")
# f.close()
#
# #File write
#
# f=open("file1.txt","w")
# f.write("Information Science and Engineering\n")
# a=f.write("Information Science and Engineering\n")
# print(a) # prints the number of character in the file
#
# # f.close()
#
# #Append
# #
# # f=open("file1.txt","a")
# # f.write("Jss Academy Of Technical Education\n")
# # #
# # f.close()
# #
# # # Read and Write both
# # f=open("file1.txt","r+")
# # print(f.read())
# # f.write("Bangalore")
#
#
# #f.seek() -> brings the pointer to the given argument as the index
#
# #f.tell()-> Tells which index the file pointer resides
#
# print(f.tell())
# # f.seek()
# # f.write("hello")
# f.close()


#With BL0CK
# with open("file1.txt","a") as f:
#     f.write("Chikmagalur")
#
# f = open("file1.txt")
# print(f.read())
# f.close()
#
# with open("file1.txt","w") as f:
#     f.write("Name:Jeevan K V\nUsn:1JS18IS039\nBranch:Ise\nsem: 4'A'\n")
# f=open("file1.txt")
# print(f.read())
# f.close()

with open("LibLog.txt") as f:
    for i in f:
        print(i)




