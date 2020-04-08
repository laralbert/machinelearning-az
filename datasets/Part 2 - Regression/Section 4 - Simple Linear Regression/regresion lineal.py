# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:44:33 2020

@author: al_la
"""


# Plantilla de regresion lineal

# Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# Importar el dataset
dataset = pd.read_csv('Salary_Data.csv')
# dataset = dataset[,2:3]

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 1].values

# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Los train y test son los sets que se usarán para entrenar y probar el modelo 

from sklearn.model_selection import train_test_split
# El text_size indica que el 20 por ciento de los datos de X se utilizarán para testear el modelo, normalmente se usa entre 20 y 30 por mucho
# random_state se usa para evitar la aleatoriedad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3 , random_state = 0)


'''
# Escaldo de variables
# Standarización, esto ayuda a que los modeos converjan mas rapidamente
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

# Crear modelo de regresión lineal simple con el conjunti de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predecir el conjunto de test
y_pred = regression.predict(X_test)

# Visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue") 
plt.title("Sueldo vs años de experiencia (Conjunto de entrenamiento)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo (en dolares)")
plt.show()

# Visualizar los resultados de testing
plt.scatter(X_test, y_test, color = "red")
# La recta es la misma para train como para test, pues que se engeneró con train
plt.plot(X_train, regression.predict(X_train), color = "blue") 
plt.title("Sueldo vs años de experiencia (Conjunto de testing)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo (en dolares)")
plt.show()



