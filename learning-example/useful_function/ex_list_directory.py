import os
def list_dir(path,level):
    for item in os.listdir(path):
        print("|    " * level + "+--" + item)
        newpath = os.path.join(path,item)
        if os.path.isdir(newpath):
            list_dir(newpath,level+1)