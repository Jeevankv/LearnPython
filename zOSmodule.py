import os

print(dir(os))

print(os.getcwd())
# os.chdir("D:\Gallery")
# print(os.getcwd())
print(os.listdir())  # gives folders in the current directory

# os.makedirs('os-demo/os-demo2') #  used to create a folders within folder
# os.mkdir()  #  used to create a single folder
# os.removedirs("os-demo/os-demo2") #used to delete tree stuctured folders
# os.rmdir() # used to delete a single folder

# os.rename("OS-demo.txt","file1.1.txt")
# os.rename("file1.1.txt","file.txt")

print(os.stat("file.txt"))  ## for knowing information of a file  like:
print(os.stat("file.txt").st_size)  ## size of file
print(os.stat("file.txt").st_mtime)  ## Last modified time
from datetime import datetime

print(os.stat("file.txt").st_mtime)  ## Last modified time
mod_time = datetime.fromtimestamp((os.stat("file.txt").st_mtime))
print(mod_time)

for current_path, directory_folder, directory_file in os.walk('D:/Movies'):
    # if "Money.Heist.S01E01 en.mkv" in directory_file:
        print("current_path", current_path)
        print("Directories", directory_folder)
        print("Files:", directory_file)
        print()

# print(os.environ.get('TMP'))

###  os.path

print(os.path.join(os.getcwd(), "os-demo.txt"))  # join easily , we do not want to care of back slashes

print(os.path.basename('/tmp/text.txt'))  # gives the base file
print(os.path.dirname('/tmp/text.txt'))  # gives the directory name
print(os.path.dirname('/tmp/text.txt'))  # gives both directory and files
print(os.path.split('/tmp/text.txt/text2.txt'))  # gives both directory and basename as tuple
print(os.path.exists('/tmp/text.txt/text2.txt')) # gives True and False based on availibilty of path

# os.path.isdir()
# os.path.isfile()

print(os.path.splitext('text.txt')) #Gives tuple with rootname and extension

print(dir(os.path))