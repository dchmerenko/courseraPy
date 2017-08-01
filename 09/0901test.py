# class Matrix
from sys import stdin


class Matrix:
    def __init__(self, *args):
        for arg in args:
            self.row = arg[:]

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.row))

    def size(self):
        return len(self.row), len(self.row[0])

exec(stdin.read())
