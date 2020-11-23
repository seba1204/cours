def ConvertDataFromCSV(path):
    """Read data from the csv given and return an numpy array filled with this data"""
    materialName = ''  # Name of the tested material
    epsilon = []  # Movemennt of the test piece
    sigma = []  # Force applied on the test piece
    starting = True

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)

    if (os.path.exists(filename)):
        try:
            file = open(filename, 'r')
            for row in file.readlines():
                try:
                    line = clearEmptyCells(row.replace('\n', '').split(';'))
                    if (starting):
                        starting = not starting
                        materialName = line[0]
                    elif (isNumeric(line)):
                        # Data reading from the CSV file
                        movement = float(line[0])
                        force = float(line[1])

                        # Formating of data
                        tranformedData = Transform(movement, force)

                        # Adding data to result that will be returned
                        epsilon.append(tranformedData[0])
                        sigma.append(tranformedData[1])
                except:
                    print('error !')
        finally:
            file.close()
        return (materialName, sigma, epsilon)
    else:
        raise ValueError("File ({}) doesn\'t exists".format(path))
