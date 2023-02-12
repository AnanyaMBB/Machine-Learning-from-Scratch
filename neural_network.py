import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, layers, units, data, activations=[]):
        self.w = []
        self.b = []
        self.layers = layers
        self.units = units
        self.data = data
        self.activations = activations
        self.Dense()

    # Activation functions
    def sigmoid(z):
        return np.exp(-z)

    # layers
    def Dense(self):
        for i in range(self.layers - 1):
            self.w.append(np.zeros((self.units[i], self.units[i+1])))
            self.b.append(np.zeros((self.units[i+1])))
        self.b = np.zeros((self.layers, ))

    # Forward propagation
    def forward_prop(self):
        a = self.data

        for i in range(self.layers - 1):
            print(a)
            print(self.w[i])
            z = np.matmul(a, self.w[i])
            a = z
        return a

    # Error

    # def forward_prop_rec(self, a, w, b):
    #     np.matmul(self.data.T, self.w) + self.b

    # Backward propagation

    # def test():
    #     print(self.w)


data = [[1, 2], [3, 4], [5, 6]]

a = NeuralNetwork(3, [2, 2, 1], np.array(data)).forward_prop()
