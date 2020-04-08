# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:24:27 2020

@author: al_la
"""


# Plantilla de datos categóricos

# Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# Importar el dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 3].values

# Codificar datos categóricos
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])


# Codificar con variables dummy
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)

le_y = preprocessing.LabelEncoder()
y = le_y.fit_transform(y)
