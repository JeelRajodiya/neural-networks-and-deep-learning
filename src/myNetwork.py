import numpy as np


class Network():

    def __init__(self, sizes) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(r, 1) for r in sizes[1:]]
        self.weights = [
            np.random.randn(r, c) for c, r in zip(sizes[:-1], sizes[1:])
        ]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a) + b)
        return a

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))


print(net.biases[0])