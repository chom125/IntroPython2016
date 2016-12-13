#!/usr/bin/env python

"""
Simple iterator examples
"""

class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """
    def __init__(self, start=0, stop=10, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current + self.step <= self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration

    def __str__(self):
        print(self.__next__())

if __name__ == "__main__":

    print("Testing the iterator:")
    for x in IterateMe_2(0, 20, 3):
        print(x)
