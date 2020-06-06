class File:
    _file = []

    def __init__(self):
        self._file = []

    def push(self, element):
        """Add element at the end of the file"""
        self._file.append(element)

    def top(self):
        """Return the first element of the file without modifying it"""
        return self._file[:1]

    def pop(self):
        """Return the first element of the file, and remove it from the file."""
        a = self._file[:1]
        self._file = self._file[1:]
        return a

    def lenght(self):
        """Return lenght of the file."""
        return len(self._file)

    def isEmpty(self):
        """Return true if file is empty."""
        return len(self._file) == 0

    def toString(self):
        """Return file in a str type"""
        return str(self._file)
