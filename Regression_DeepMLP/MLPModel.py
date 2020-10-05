#!pip install -q -U keras-tuner
import tensorflow as tf
from tensorflow import keras
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
import kerastuner as kt
from kerastuner import HyperModel
from kerastuner import HyperParameters

#define the model using HyperModel
class DeepMLPModel(HyperModel):

    #takes the input shape of the data
    def __init__(self, input_shape):
        self.input_shape = input_shape
    
    #build the model with choice for hyperparameters values
    def build(self, hp):
        model = Sequential()

        #first layer
        model.add(Dense(units = hp.Choice('units_hidden1', 
                                          values = [128, 64, 32, 16, 8], 
                                          default = 32),
                        #units = hp.Int('units', 8, 64, 4, default=32),
                        activation=hp.Choice('dense_activation1',
                                              values = ['relu', 'tanh','sigmoid'],
                                              default='relu'),
                        input_shape = self.input_shape,
                        )
        ) 
        
        #dropout layer
        model.add(Dropout(hp.Choice('dropout1',
                                    values = [0.0, 0.1, 0.2],
                                    default = 0.0)
                         )
        )

        #hidden layers upto 4 layers
        for i in range(hp.Int('num_layers', 1, 4)): 
            model.add(Dense(units=hp.Choice('units_hidden2', 
                                             values = [64, 32, 16, 8], 
                                             default = 32),
                            activation=hp.Choice('dense_activation2',
                                                  values = ['relu', 'tanh','sigmoid'],
                                                  default = 'relu'),
                          )
          )

        #dropout layer
        model.add(Dropout(hp.Choice('dropout2',
                                    values = [0.0, 0.1, 0.2],
                                    default = 0.0)
                         )
        )

        model.add(Dense(units=hp.Choice('units_hidden3', 
                                          values = [16, 8], 
                                          default = 8),
                          activation=hp.Choice('dense_activation3',
                                                values = ['relu', 'tanh','sigmoid'],
                                                default = 'relu'),
                          )
        )

        #final layer
        model.add(Dense(1))
        
        #compile the model
        model.compile(
            optimizer = hp.Choice('optimizer', 
                                   values = ["adam", "sgd", "rmsprop"], 
                                   default = "adam"),
            loss='mse',
            metrics=['mae']
        )
        
        return model
