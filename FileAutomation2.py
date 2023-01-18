import os
from sys import *

def RenameFileExtension(path, ext1, ext2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if(exists):
        for dirName, subdirs, fileList in os.walk(path):

            for filen in fileList:
                path = os.path.join(dirName, filen)
                if filen.endswith(ext1):
                    newfile = filen.replace(ext1,ext2)
                    os.rename(os.path.join(dirName, filen),os.path.join(dirName, newfile))
                    flag = True
        if flag:
            print("All files renamed Successfully")
        else:
            print("No files with such extension")
    else:
        print("Invalid Path")

def main():
    print()

    if(len(argv) != 4):
        print("Insufficient Arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script will traverse the specific directory and rename the file extensions.")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_name AbsolutePath_Of_Directory Extension1 Extension2")
        exit()

    try:
        arr = RenameFileExtension(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of Input.")

    except Exception as E:
        print("Error : Invalid Input : ",E)

if __name__ == "__main__":
    main()