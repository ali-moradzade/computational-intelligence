import numpy as np


def activation(x):
    """
    The activation function of our neural network, e.g., Sigmoid, ReLU.
    :param x: Vector of a layer in our network.
    :return: Vector after applying activation function.
    """
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        input_layer = layer_sizes[0]
        hidden_layer = layer_sizes[1]
        output_layer = layer_sizes[2]

        w1 = np.random.normal(size=(hidden_layer, input_layer))
        w2 = np.random.normal(size=(output_layer, hidden_layer))

        b1 = np.random.normal(size=(hidden_layer, 1))
        b2 = np.random.normal(size=(output_layer, 1))

        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer

        self.w1 = w1
        self.w2 = w2

        self.b1 = b1
        self.b2 = b2

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        x = x.reshape((self.input_layer, 1))

        a1 = activation(self.w1 @ x + self.b1)
        a2 = activation(self.w2 @ a1 + self.b2)

        return a2
