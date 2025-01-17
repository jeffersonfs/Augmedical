import random


class ImageTransform:
    def __init__(self, p):
        self.p = p

    def apply(self, x):
        return x

    def __call__(self, sample):
        if random.random() <= self.p:
            sample = self.apply(sample)

        return sample
