import numpy as np


def ground(x):
    1


class Stage:
    def __init__(self, height, length):
        self._height = height
        self._length = length
        self._map = np.zeros((height, length))

    def stage(self):
        print("stage")
        print(self._map)

    def save(self):
        print("saving")
        np.savetxt("stage1.dat", self._map)

    def create_map(self):
        np.apply_along_axis(ground, 1, self._map)
        print(self._map)
