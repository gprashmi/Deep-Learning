"""

This file implements Neural Network from scratch that includes adding multiple layers, different activation functions, feed forward, calculating MSE loss, back propagation, weight and bias updates and finally predicting on the test data.

Class Layer implements different layers, initialization of weights and bias for each layer, perform dot product of the input to get the predicted output by applying activations in each layer and also determines the derivative of activation function for the backpropagation.

Class Neural Network implements feed forward and back propagation for training the network, predicting on the test data, perform early stopping if required.

"""

#import libraries
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

#define Layer class to add layers to the neural network
class Layer:
 
    def __init__(self, in_neruons, out_neurons, activation_func = 'tanh'):
        """
        Args:
        
        in_neruons(int): number of input neurons in this layer
        out_neurons(int): number of output neurons in this layer
        activation_func(str): activation function to be used
        wts: weights of the layer, chosen randomly
        bias: bias for the layer, chosen randomly

        """
        #set a random state 
        np.random.seed(42)
        #initialize weights and bias for the layer
        self.wts = np.random.rand(in_neruons, out_neurons)
        self.bias = np.random.rand(out_neurons)
        self.activation_func = activation_func
        self.prev_activation = None
        self.error = None
        self.error_delta = None
    
    #calcuate the dot product of input and the weights of the layer
    def activate(self, x):
        """
        Args:
        
        x: input of the layer

        return value: the activated function output of the dot product

        """
        r = np.dot(x, self.wts) + self.bias
        self.prev_activation = self.apply_act_func(r)
        return self.prev_activation
    
    #apply the activation function after the dot product of input and weights for this layer
    def apply_act_func(self, r):
        """
        Args

        r: the dot product result from the activate function

        return value: the activated result

        """
        #Activation function: tanh
        if self.activation_func == 'tanh':
            return np.tanh(r)
        
        #Activation function: relu
        if self.activation_func == 'relu':
            return np.maximum(0,r)

        #Activation function: sigmoid
        if self.activation_func == 'sigmoid':
            return 1 / (1 + np.exp(-r))

        return r
    
    #calculate the derivative of the activation function required in back propagation
    def act_func_derivative(self, r):
        """
        Args:
        
        r: input for which activation func derivated needs to be calculated

        return value: derived value of the activated function

        """        
        #Activation function: tanh
        if self.activation_func == 'tanh':
            return 1 - r ** 2
        
        #Activation function: relu
        if self.activation_func == 'relu':
            r[r<=0] = 0
            r[r>0] = 1
            
            return r

        #Activation function: sigmoid
        if self.activation_func == 'sigmoid':
            return r * (1 - r)

        return r


#define the neural network class
class NeuralNetwork:

    def __init__(self):
        self.layers = []

    #function to add layers to the NN
    def add_layer(self, layer):
        """

        Args:
        
        layer: layer to add to the nn 
        
        """

        self.layers.append(layer)
    
    #MSE loss function
    def mse_loss(self,X,y):
        """
        Args:
        
        X: input data
        y: target data
        
        return: MSE loss between the target and predicted output
        """
        
        return np.mean(np.square(y - self.feed_forward(X)))
       
    #perform feed forward to calculate the predicted output
    def feed_forward(self, X):
        """
        
        Args:
        
        X: input data

        return: feed forwarded ouput

        """
        
        #iterate through the layers of the NN
        for layer in self.layers:
            #call the activate function to calculate the feed forward output
            X = layer.activate(X)
        return X
    
    #perform back propagation to update the weights, bias and thus train the network
    def backpropagation(self, X, y, pred_out, learning_rate):
        """
        Args:
        
        X: input data
        y: target data
        pred_out: predicted output from feed forward
        learning_rate(float): the step_size to increment/decrement the weights and bias 

        """

        #iterate over the layers in reverse direction to update weights/bias
        for i in reversed(range(len(self.layers))):
            layer = self.layers[i]
            
            #if current layer is the last output layer
            if layer == self.layers[-1]:
                #calculate the error between target and predicted output
                layer.error = y - pred_out
                # The output = layer.last_activation in this case
                #based on the formula for BP, error derivative/wt = layer.error * act_func_derivative
                layer.error_delta = layer.error * layer.act_func_derivative(pred_out)
            else:
                #go the next previous layer to the current layer
                prev_layer = self.layers[i + 1]
                #calculate the error between prev layer weights and the prev layer delta
                layer.error = np.dot(prev_layer.wts, prev_layer.error_delta)
                #calcuate the error_delta for the current layer based on the formula in the markdown
                layer.error_delta = layer.error * layer.act_func_derivative(layer.prev_activation)

        #update the weights and bias
        for i in range(len(self.layers)):
            layer = self.layers[i]
            input_data = np.atleast_2d(X if i == 0 else self.layers[i - 1].prev_activation)
            layer.wts += layer.error_delta * input_data.T * learning_rate
            layer.bias += layer.error * input_data.T * learning_rate
        
    #train the NN
    def train(self, X, y, learning_rate, max_epochs,early_stopping = False):
        """

        Args:

        X: input data
        y: target data
        learning_rate(float): the step_size to increment/decrement the weights and bias 
        max_epochs(int): the number of epochs for which the NN is trained

        return value: MSE loss for each epoch

        """
        
        loss = float('inf')
        patience = 0
        mse_loss = []
        
        #iterate for each epoch
        for i in range(max_epochs):
            #iterate for each data instance
            for j in range(len(X)):
                
                #feed forward propagation
                pred_out = self.feed_forward(X[j])
                
                #back propagation
                self.backpropagation(X[j], y[j], pred_out, learning_rate)
            
            mse,acc = self.mse_loss(X,y),5
            mse_loss.append(mse)
            
            #print the results for every 10 epochs
            if i % 10 == 0:
                print_mse = round(self.mse_loss(X,y),5)
                pred_list = self.predict(X)
                print_acc = accuracy_score(y,pred_list)
                print("Epoch: {}, loss: {:.5f}, Training accuracy:{:.5}".format(i,print_mse,print_acc))
                           
                if early_stopping == True:
                    if print_mse < loss:
                        patience = 0
                        loss = print_mse
                    else:
                        patience += 1
                        loss = print_mse

                    if patience > 3:
                        print("Early stopping")
                        break
                    else:
                        continue

        return mse_loss
    
    #function to predict on test data
    def predict(self, X):
        """

        Args:
        
        X: test data 

        return value: predicted output

        """
        
        #feed forward the test data
        y_pred_proba = self.feed_forward(X)
        
        #store the final predicted values
        pred_list = []

        #perform thresholding on the y_pred_proba
        for i in range(len(y_pred_proba)):
            if y_pred_proba[i] >= 0.5:
                pred = 1
            else:
                pred = 0

            pred_list.append(pred)
        
        return pred_list