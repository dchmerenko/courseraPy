from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lst):
        self.m = deepcopy(lst)

    def __str__(self):
        rows = []
        for row in self.m:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        return len(self.m), len(self.m[0])


exec(stdin.read())
