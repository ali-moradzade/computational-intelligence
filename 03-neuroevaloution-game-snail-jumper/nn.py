import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def leaky_relu(x):
    return np.maximum(0.01 * x, x)


def tanh(x):
    return np.tanh(x)


def softmax(x):
    e_x = np.exp(x)
    return e_x / e_x.sum(axis=0)


def linear(x):
    return x


def choose_activation(function):
    if function == "sigmoid":
        return sigmoid
    elif function == "tanh":
        return tanh
    elif function == "relu":
        return relu
    elif function == "leaky-relu":
        return leaky_relu
    elif function == "softmax":
        return softmax
    elif function == "linear":
        return linear
    else:
        raise ValueError('Activation function not found')


def activation(x, function='sigmoid'):
    """
    The activation function of our neural network, e.g., Sigmoid, ReLU.
    :param function: Kind of activation function we want
    :param x: Vector of a layer in our network.
    :return: Vector after applying activation function.
    """
    return choose_activation(function)(x)


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        self.input_layer = layer_sizes[0]
        self.hidden_layer = layer_sizes[1]
        self.output_layer = layer_sizes[2]

        self.w1 = np.random.standard_normal(size=(self.hidden_layer, self.input_layer))
        self.w2 = np.random.standard_normal(size=(self.output_layer, self.hidden_layer))

        self.b1 = np.zeros((self.hidden_layer, 1))
        self.b2 = np.zeros((self.output_layer, 1))

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

    def __str__(self):
        return 'w1:\n{},\nw2:\n{},\nb1:\n{},\nb2:\n{}'.format(self.w1, self.w2, self.b1, self.b2)
