# class Matrix
from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, *args):
        for arg in deepcopy(args):
            self.row = arg

    def __str__(self):
        s_matrix = list()
        for r in self.row:
            s_row = '\t'.join(map(str, r))
            s_matrix.append(s_row)
        return '\n'.join(s_matrix)

    def size(self):
        return len(self.row), len(self.row[0])

exec(stdin.read())
