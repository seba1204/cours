import os.path


def pat(p):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, '..', p)
