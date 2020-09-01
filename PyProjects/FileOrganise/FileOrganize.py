
import os
def organize(path, file, format):
    os.chdir(path)
    files = os.listdir()
    print(files)
    i = 1
    with open(file) as f:
        filelist = f.read().split("\n")
        print(filelist)

    for file in files:
         if file not in  filelist:
            os.rename(file, file.capitalize())

         if os.path.splitext(file)[1] == format:
               os.rename(file,f"{i}{format}")
               i+=1



organize("D:\Document\PyCharm\LearnPy\PyProjects\FileOrganise\Test","D:\Document\PyCharm\LearnPy\PyProjects\FileOrganise\dont_change.txt",".png")
