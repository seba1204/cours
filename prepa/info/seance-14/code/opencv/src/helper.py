import os


def listify(list1, list2):
    if (type(list1) != list):
        list1 = [list1]
    if (type(list2) != list):
        list2 = [list2]
    if (len(list1) != len(list2)):
        raise Exception('list1 and list2 must have the same size !')
    data = []
    for i in range(len(list1)):
        data.append((list1[i], list2[i]))
    return (data)


def pat(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, '..', path)
