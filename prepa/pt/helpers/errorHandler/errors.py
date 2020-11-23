class Error(Exception):
  """Base class for exceptions in this module."""
  pass

class UnexistFile(Error):
  """Exception raised for errors in openning CSV.

  Attribute:
    path -- path of the unknow file
  """

  def __init__(self, path):
    self.message = 'The file \"{}\" doesn\'t exists'.format(path)