import numpy as np
from log_kw.log_kmedoid import k_medoid, Dot


class KmAlg:
    def __init__(self, data: list, k_classes):
        self.data = data
        self.k_classes = k_classes
        self.result = k_medoid(self.data, self.k_classes)
        self._medoids = self.find_medoids()
        self._counter = 10

    def find_medoids(self):
        res = []
        for i in self.result:
            if i[2]:
                res.append(i)
            if len(res) == self.k_classes:
                return res

        while len(res) < self.k_classes:
            res.append(self.result[0])
        return res

    def append(self, other):
        if type(other[0]) is list:
            for i in other:
                self.data.append(i)
                self.result.append([i, self.nearest_medoid(i), False])
            self._counter -= len(other)

        else:
            self.data.append(other)
            self._counter -= 1
            self.result.append([other, self.nearest_medoid(other), False])

        if self._counter < 1:
            self.result = k_medoid(self.data, self.k_classes)
            self._medoids = self.find_medoids()
            self._counter = 10
        return self.result

    def nearest_medoid(self, other):
        dot = Dot(other)
        medoids = [Dot[i] for i in self._medoids]
        res = [dot + i for i in medoids]
        return res.index(min(res))
