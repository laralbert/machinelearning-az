# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:15:02 2020

@author: al_la
"""


# Plantilla de preprocesado

# Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# Importar el dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 3].values

'''
# Tratamiento de los nan
from sklearn.impute import SimpleImputer
# reemplazar por medias
imputer = SimpleImputer(strategy = "mean")
# medias en columns 1 y 2, la 0 no es numérica
imputer = imputer.fit(X[: , 1:3])
# Cambiar valores por dichas medias
X[:, 1:3] = imputer.transform(X[:, 1:3])
'''
'''
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
'''

# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# # Escaldo de variables
# # Standarización, esto ayuda a que los modeos converjan mas rapidamente
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)











