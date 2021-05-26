The sinking of the Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

The objective of this project is to predict survival of the passengers by implementing a neural network from scratch and compare its performance with different ensemble models built using Logistic Regression, Gradient Boosting and MLP classifiers.

Dataset:

The dataset is taken from Kaggle where the train has 891 instances with 10 feature columns and 1 dependent column (Survived) and the test data has 418 instances. The following methods are used for data cleaning and pre-processing:
1. Feature Selection: 
    1. Family_size, Total_fare and Title are extracted from Parch, SibSp, Fare, Name
    2. PassengerID, Name, Fare, SipSp, Parch, Ticket, Cabin features are dropped
2. Data cleaning:
    1. Encode categorical features into integers using Ordinal Encoder. Imputing missing values after performing one-hot encoding may give inaccurate results as this approach will generate more features and the imputation for categorical features will vary because of the sparsity. To eliminate this problem, OE is used to convert non-null values to integers preserving the NaN values and this can be converted back to strings for one-hot encoding later on.
    2. Using mean on Age feature and mode on Sex, Embarked results in filling values based on that particular column values. It does not consider the relation with other features. Thus Iterative Imputer is used, which model each feature with missing values as a function of other features in a round-robin fashion. It performs imputation for certain steps by fitting a regression line on (X,y) for known values where y is missing value feature and X are other columns. By using this line, missing values are imputed and this is done for each feature
3. Data Pre-processing:
    1. After data cleaning is performed, the categorical features are converted back to string values and using pd.get_dummies the features: Sex, Embarked and Title are one-hot encoded that creates one binary variable for each category
    2. Standard Scaler is used which scales the features using its mean and standard deviation

Modelling

Four algorithms are implemented in this project:

1. Neural Network: NN model is implemented from scratch using Python incorporating adding multiple layers, different activation functions, feed forward, MSE loss calculation and back propagation, and early stopping to avoid overfitting. the below flow chart and the points shows the process followed to implement NN:
    1. Prepare data and create a NN model using different layers, neurons, and activation functions. Train the network.
    2. Apply feed forward to calculate the o/p, calculate the MSE loss and perform back-propagation to update weights and bias so as to reduce the loss.

2. Voting Classifier Model: It is an ensemble based ML model that trains on multiple unfitted-algorithms using hard/soft voting method. Here 3 such ML models: LR, GBC and MLPC are used to preform ensemble voting classifier with “hard” voting using sklearn library. The “hard” voting approach predicts output based on the highest probability among the models for the chosen class and gives the output.

3. Average and Weighted Average Ensemble Model: The main reason for using average and weighted average ensemble modeling is to reduce the error by aggregating the predictions over multiple classifiers. Assuming every classifier makes mistakes in prediction and by using diverse classifiers such as simple ML model (LR), ensemble algorithm (GBC) and neural network (MLPC) and by aggregating their predictions, we can try to reduce the prediction error.
    1. Average Ensemble: This approach averages the predictions on the validation set from all the models considered for ensemble and the average prediction is used to evaluate the performance.
    2. Weighted Average: This method assigns weights to the classifier predictions, higher value for better classifiers and smaller values for other classifiers and then calculates the weighted average prediction to reduce the error loss
