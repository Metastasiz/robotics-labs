from pathlib import Path
import sys
import re

def getPath(main_dir, path_to_target = "", max_subDir = 10):
    
    path_parent = Path().resolve()

    for _ in range(max_subDir):
        if re.search(main_dir+"$",str(path_parent)):
            break
        path_parent = path_parent.parent

    if path_to_target.count("\\") > path_to_target.count("/"):
        path_to_target = path_to_target.split("\\")
    if path_to_target.count("\\") < path_to_target.count("/"):
        path_to_target = path_to_target.split("/")

    for dir_ in path_to_target:
        path_parent = path_parent / dir_

    return path_parent

def appendPath(main_dir, path_to_target = "", max_subDir = 10):
    sys.path.append(str(getPath(main_dir, path_to_target)))
