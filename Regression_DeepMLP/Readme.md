# House Price Prediction using Deep MLP

The objective is to build a Deep MLP model to predict the house value for the California Housing dataset based on different attributes. The data set consists of 8 features and about 20000 instances. 

### Modelling

The MLP neural network is built using Keras and Tensorflow in Python. Since MSE, MAE metrics and normalization of data points are affected by the presence of outliers, initially a simple 2 layer MLP model is trained with and without outliers to verify outlier effect on the results. The performance of the model without outliers was better compared to the model with outliers and thus tuning and rest of the modeling was done on data without outliers. 

To achieve better results for a neural network, its hyper-parameters are to be tuned and doing this manually is a tedious and time consuming process. The hyper-parameters tuned are: number of layers, neurons, activation functions, optimizer and learning rate. Thus this notebook uses Keras Tuner library to perform hyper-parameter tuning and the tuner process is as shown in the figure. The hyper model is defined with the combinations and choice of the parameters to be searched and tuned. The tuner runs for defined trails to perform the search and give the best parameters. 

The tuning is performed using 
1. RandomSearch Tuner: It randomly selects the parameter values, build the model and tries to minimize the objective function. 
2. HyperBand Tuner: It uses adaptive resource allocation and early-stopping to quickly converge on a high-performing model. The algorithm trains a large number of models for a few epochs and carries forward only the top-performing half of models to the next round.

Using the best model achieved, I tried to use LeakyReLU and SeLU activations on the best model parameters to check for the results.

### Results

The results of the model performance are tabulated and the time taken by RandomSearch tuner was about 20mins where as HyperBand tuner took about 34mins to search for the best model.


|Model                          |MSE    |RMSE   | MAE   |
|-------------------------------|-------|-------|-------|
|Baseline with Outliers         |0.4673 |0.6836 |0.4998 |
|Baseline without outliers      | 0.2658|0.5156 | 0.3897|
|RandomSearch Tuner             | 0.2196|0.4686 |0.3328 |
|HyperBand Tuner                |0.1990 |0.4461 |0.3147 |
|Model with LeakyRelu activation|0.3816 |0.6177 |0.4804 |
|Model with SeLU activation     |0.8127 |0.9065 |0.7641 |

There is considerable difference between the baseline model (2 layer NN) and the tuned models. However, the models with LeakyReLU and SeLU did not perform well indicating they do not suit for the regression problem of this dataset. Therefore the best model turns out to have 25.13% decrease in the test error that was tuned by HyperBand compared to the baseline model without outlier. 

### References

1. https://keras-team.github.io/keras-tuner/\

2. https://www.tensorflow.org/tutorials/keras/keras_tuner\
