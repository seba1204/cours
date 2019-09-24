import os.path


def openCSV(path):
  if (os.path.exists(path)):
    try:
      file = open(path, 'r')
      for row in file.readlines():
        try:
          print(row.split(';'))
        except:
            pass
    finally:
      file.close()

  else:
    raise ('Le fichier {} n\'existe pas'.format(path))

openCSV('data.csv')