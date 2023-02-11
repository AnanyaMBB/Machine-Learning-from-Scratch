import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, layers, units, data):
        self.w = []
        self.b = []
        self.layers = layers
        self.units = units
        self.data = data

    # Activation functions
    def sigmoid(z):
        return np.exp(-z)

    # layers
    def Dense(self):
        for i in range(self.layers - 1):
            self.w.append(np.zeros((self.units[i], self.units[i+1])))
            self.b.append(np.zeros())
        self.w = np.array(self.w)
        self.b = np.zeros((self.layers, ))

    # Forward propagation
    def start_forward_prop(self):
        for i in range(self.layers):
            self.forward_prop(self, self.data, self.w, self.b)

    def forward_prop(self, a, w, b):
        np.matmul(self.data.T, self.w) + self.b

    # Backward propagation

    # def test():
    #     print(self.w)


a = NeuralNetwork(3, [2, 3, 1])
print(a.w)
