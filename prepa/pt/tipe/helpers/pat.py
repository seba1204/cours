import os


def getExt(path):
    return os.path.splitext(path)[1]


def getName(path):
    return os.path.splitext(os.path.basename(path))[0]


def getPath(path):
    return os.path.splitext(path)[0]


def getNameWithExt(path):
    return os.path.basename(path)
