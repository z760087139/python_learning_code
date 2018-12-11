# to find regodic a path
# os.walk is a generate return the directories and files in current path
# and walk down to each directory
import os
path = os.getcwd()
for dirpath,dirnames,filenamse in os.walk(path):
    for file in filenamse:
        file_fullname = os.path.join(dirpath,file)
    # current directory == dirpath
    
