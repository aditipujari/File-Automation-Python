import os
from sys import *

def FindFileWithExtension(path, ext):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if(exists):
        for dirName, subdirs, fileList in os.walk(path):

            for filen in fileList:
                path = os.path.join(dirName, filen)
                if filen.endswith(ext):
                    print("File with extension {} is {} in {}".format(ext,filen,dirName) )

    else:
        print("Invalid Path")

def main():
    print("--------------Application-----------------")

    if(len(argv) != 3):
        print("Insufficient Arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script will traverse the specific directory and display the files with the same extension as given in input.")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_name AbsolutePath_Of_Directory Extension")
        exit()

    try:
        arr = FindFileWithExtension(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of Input.")

    except Exception as E:
        print("Error : Invalid Input : ",E)

if __name__ == "__main__":
    main()