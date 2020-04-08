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
# dataset = dataset[,2:3]

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 3].values


# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Los train y test son los sets que se usarán para entrenar y probar el modelo 

from sklearn.model_selection import train_test_split
# El text_size indica que el 20 por ciento de los datos de X se utilizarán para testear el modelo, normalmente se usa entre 20 y 30 por mucho
# random_state se usa para evitar la aleatoriedad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0)


'''
# Escaldo de variables
# Standarización, esto ayuda a que los modeos converjan mas rapidamente
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''









