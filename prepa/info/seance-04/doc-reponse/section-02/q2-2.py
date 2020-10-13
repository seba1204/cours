def clearEmptyCells(inputList):
    """
        @inputs  : list
        @returns : same list without empty cells
    """
    return [k for k in inputList if k != '']
