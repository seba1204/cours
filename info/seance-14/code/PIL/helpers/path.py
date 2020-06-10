import os


def r(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, '..', path)
