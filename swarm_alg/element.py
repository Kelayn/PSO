import numpy as np


class Element():
    def __init__(self, dimension, min_border, max_border):
        self.position = np.random.rand(dimension) \
                        * (max_border - min_border) + min_border
        self.b_local_pos = self.position
        self.b_local_val = float("-inf")
        self.min_border = min_border
        self.max_border = max_border

        velocity_magical_coef = 2 * (max_border - min_border)  # WHY ??
        self.velocity = np.random.rand(dimension) \
                        * (velocity_magical_coef ) + min_border

    def move(self):
        self.position = self.position + self.velocity