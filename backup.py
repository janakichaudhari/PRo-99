import os
import shutil

source=input("enter the source folder:")
dest=input("enter you file destination: ")

source=source+'/'
dest=dest+'/'
listfile=os.listdir(source)
for k in listfile:
    shutil.copy((source+k),dest)