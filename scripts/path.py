#pretty much just to parse the first system arg to simplify opening related files
import sys
import os

def getpath():
    path=os.path.split(sys.argv[0])
    return path[0]

cwd=getpath()