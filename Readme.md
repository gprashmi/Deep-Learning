{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red0\green0\blue0;\red191\green191\blue191;
}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;\csgray\c79525;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # House Price Prediction using Deep MLP\
\
The objective is to build a Deep MLP model to predict the house value for the California Housing dataset based on different attributes. The data set consists of 8 features and about 20000 instances. \
\
### Modelling\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 The MLP neural network is built using Keras and Tensorflow in Python. Since MSE, MAE metrics and normalization of data points are affected by the presence of outliers, initially a simple 2 layer MLP model is trained with and without outliers to verify outlier effect on the results. The performance of the model without outliers was better compared to the model with outliers and thus tuning and rest of the modeling was done on data without outliers. \
\
To achieve better results for a neural network, its hyper-parameters are to be tuned and doing this manually is a tedious and time consuming process. The hyper-parameters tuned are: number of layers, neurons, activation functions, optimizer and learning rate. Thus this notebook uses Keras Tuner library to perform hyper-parameter tuning and the tuner process is as shown in the figure. The hyper model is defined with the combinations and choice of the parameters to be searched and tuned. The tuner runs for defined trails to perform the search and give the best parameters. \
\
The tuning is performed using \
1. RandomSearch Tuner: It randomly selects the parameter values, build the model and tries to minimize the objective function. \
2. HyperBand Tuner: It 
\f1 \cb2 \expnd0\expndtw0\kerning0
uses adaptive resource allocation and early-stopping to quickly converge on a high-performing model. The algorithm trains a large number of models for a few epochs and carries forward only the top-performing half of models to the next round.\
\
Using the best model achieved, I tried to use LeakyReLU and SeLU activations on the best model parameters to check for the results.\
\
### Results\
\
The results of the model performance are tabulated and the time taken by RandomSearch tuner was about 20mins where as HyperBand tuner took about 34mins to search for the best model.\

\f0 \cb1 \kerning1\expnd0\expndtw0 \

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 Model\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 MSE\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 RMSE\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 MAE\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
Baseline with Outliers
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.4673\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.6836\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.4998\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
Baseline without outliers
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.2658\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.5156\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.3897\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
RandomSearch Tuner
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.2196\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.4686\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.3328\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
HyperBand Tuner
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.1990\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.4461\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.3147\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
Model with LeakyRelu activation
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.3816\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.6177\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.4804\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth3600\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx2160
\clvertalc \clshdrawnil \clwWidth1260\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx4320
\clvertalc \clshdrawnil \clwWidth1200\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx6480
\clvertalc \clshdrawnil \clwWidth3840\clftsWidth3 \clbrdrt\brdrs\brdrw20\brdrcf4 \clbrdrl\brdrs\brdrw20\brdrcf4 \clbrdrb\brdrs\brdrw20\brdrcf4 \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl100 \clpadr100 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
Model with SeLU activation
\f0 \cb1 \kerning1\expnd0\expndtw0 \cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.8127\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.9065\cell 
\pard\intbl\itap1\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\qr\partightenfactor0
\cf0 0.7641\cell \lastrow\row
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f1 \cf0 \cb2 \expnd0\expndtw0\kerning0
there is considerable difference between the baseline model (2 layer NN) and the tuned models. However, the models with LeakyReLU and SeLU did not perform well indicating they do not suit for the regression problem of this dataset. Therefore the best model turns out to have 25.13% decrease in the test error that was tuned by HyperBand compared to the baseline model without outlier. 
\f0 \cb1 \kerning1\expnd0\expndtw0 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
### References\
\
1. https://keras-team.github.io/keras-tuner/\
\
2. https://www.tensorflow.org/tutorials/keras/keras_tuner\
}