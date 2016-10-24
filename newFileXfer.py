import shutil
import os
#from os import path
from datetime import datetime
from datetime import timedelta


###############################

def copyOver(src, now, des):
    sourceFiles = os.listdir(src)
    for file in sourceFiles:
        if file.endswith(".txt"):
            timeModified = datetime.fromtimestamp(os.path.getmtime(src + file))
            timeDiff = (now - timeModified)
            print (timeDiff)
            if timeDiff > timedelta(days=1):
                print ("Status: Old")
                print (file)
            else:
                print ("Status: New")
                shutil.copy(src + file,des)
                print (file)

            


###############################
###change the path source and destination
###to the applicable folders on your system
def main():
    src = ("C:/Users/jmvan/Desktop/Folder A/")
    des = ("C:/Users/jmvan/Desktop/Folder B/")
    now = datetime.now()
    copyOver(src, now, des)

if __name__=='__main__':
    main()
   
