import os
from sys import *
import shutil

def CopyDirectory(dir1, dir2, ext):
    flag = os.path.isabs(dir1)
    if flag == False:
        path = os.path.abspath(dir1)

    exists = os.path.isdir(dir1)

    new_dir = os.path.join(os.getcwd(),dir2)
    os.mkdir(new_dir)

    if (exists):
        for dirName, subdirs, fileList in os.walk(dir1):

            for filen in fileList:
                if(filen.endswith(ext)):
                    path = os.path.join(dirName, filen)
                    shutil.copy2(path, dir2)
                    flag = True

        if flag:
            print("All files copied in new directory with provided extension Successfully")
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
        print("This script will traverse the specific directory and copy the contents of existing directory into a new directory.")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_name Existing_DirectoryName New_DirectoryName")
        exit()

    try:
        CopyDirectory(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of Input.")

    except Exception as E:
        print("Error : Invalid Input : ",E)

if __name__ == "__main__":
    main()