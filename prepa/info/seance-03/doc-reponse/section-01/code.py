class Pile:
    _pile = []

    def __init__(self):
        self._pile = []

    def stack(self, element):
        """Add element at the end of the pile"""
        self._pile.append(element)

    def top(self):
        """Return the last element of the pile without modifying it"""
        return self._pile[-1:]

    def unstack(self):
        """Return the last element of the pile, and remove it from the pile."""
        return self._pile.pop()

    def lenght(self):
        """Return lenght of the pile."""
        return len(self._pile)

    def isEmpty(self):
        """Return true if pile is empty."""
        return len(self._pile) == 0

    def toString(self):
        """Return pile in a str type"""
        return str(self._pile)
