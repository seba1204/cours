def isNumeric(inputList):
    """Return true if all elements in a list are numeric (int or float)"""
    for element in inputList:
        try:
            float(element)
        except:
            return False
    return True
