import numpy as np


def logistic(x):
    return 1.0 / (1 + np.exp(-x))


def logistic_deriv(x):
    return logistic(x) * (1 - logistic(x))


class MultiLayerPerceptron():
    def __init__(self, params):
        self.input_layer = params['inputLayer']
        self.hidden_layer = params['hiddenLayer']
        self.output_layer = params['numberOfClasses']
        self.learning_rate = params['learningRate']
        self.max_epochs = params['maxEpochs']
        self.bias_hidden_value = -1
        self.bias_output_value = -1

        self.weight_hidden = np.random.uniform(0, 1, (self.input_layer, self.hidden_layer))
        self.weight_output = np.random.uniform(0, 1, (self.hidden_layer, self.output_layer))
    
        self.bias_hidden = np.array(
            [self.bias_hidden_value for i in range(self.hidden_layer)])
        self.bias_output = np.array(
            [self.bias_output_value for i in range(self.output_layer)])
        self.classes_number = 3

    def starting_weights(self, x, y):
        return [[2 * np.random.random() - 1 for i in range(x)] for j in range(y)]

    def fit(self, X, y):
        for epoch in range(self.max_epochs):
            total_error = 0
            for index, inputs in enumerate(X):

                # Forward Propagation
                output_l1 = logistic(
                    np.dot(inputs, self.weight_hidden) + self.bias_hidden.T)

                output_l2 = logistic(
                    np.dot(output_l1, self.weight_output) + self.bias_output.T)

                target_output = np.zeros(self.output_layer)
                # y[index] stores the number of the correct class, numbering starts from 0
                target_output[round(y[index])] = 1

                square_error = 0
                for i in range(self.output_layer):
                    square_error = square_error + \
                        (target_output[i] - output_l2[i])**2
                square_error = square_error / self.output_layer
                total_error = total_error + square_error

                self.backpropagation(
                    target_output, output_l2, output_l1, inputs)

            total_error = (total_error / len(X))
            if (epoch % 50 == 0):
                print("Epoch #", epoch, "- Total Error: ", total_error)

    def backpropagation(self, target_output, output_l2, output_l1, x):
        error_output = target_output - output_l2
        signal_error = -1 * error_output * logistic_deriv(output_l2)

        for i in range(self.hidden_layer):
            for j in range(self.output_layer):
                self.weight_output[i][j] -= self.learning_rate * \
                    signal_error[j] * output_l1[i]
                self.bias_output[j] -= self.learning_rate * signal_error[j]

        delta_hidden = np.matmul(
            self.weight_output, signal_error) * logistic_deriv(output_l1)

        for i in range(self.input_layer):
            for j in range(self.hidden_layer):
                self.weight_hidden[i][j] -= self.learning_rate * \
                    delta_hidden[j] * x[i]
                self.bias_hidden[j] -= self.learning_rate * delta_hidden[j]

    def predict(self, X, y):
        my_predictions = []
        forward = np.matmul(X, self.weight_hidden) + self.bias_hidden
        forward = np.matmul(forward, self.weight_output) + self.bias_output

        for i in forward:
            my_predictions.append(max(enumerate(i), key=lambda x: x[1])[0])

        print("Number of Sample | Class | Output | Valid Output")
        for i in range(len(my_predictions)):
            print("#:{} | {} | Valid: {}".format(i, my_predictions[i], y[i]))

        return my_predictions
