import os
def getRelativePath():
    path = os.path.dirname(os.path.realpath(__file__))
    #replace backslash with forward slash
    path = path.replace("\\", "/")
    #remove the last word until slash
    path = path[:path.rfind("/")]
    return path