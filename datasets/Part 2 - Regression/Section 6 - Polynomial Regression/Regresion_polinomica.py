# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:49:26 2020

@author: al_la
"""


# Plantilla de Regresión polinómica

# Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# 65
# Importar el dataset
dataset = pd.read_csv('Position_Salaries.csv')
# dataset = dataset[,2:3]
# 1:"  para mandar una matriz en lugar de un vector
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# No se divide por que tenemos muy poca informacion en este ejemplo
'''
# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Los train y test son los sets que se usarán para entrenar y probar el modelo 

from sklearn.model_selection import train_test_split
# El text_size indica que el 20 por ciento de los datos de X se utilizarán para testear el modelo, normalmente se usa entre 20 y 30 por mucho
# random_state se usa para evitar la aleatoriedad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0)
'''

'''
# Escaldo de variables
# Standarización, esto ayuda a que los modeos converjan mas rapidamente
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

# 66
# Ajustar la regresion lineal con el dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)


# Ajustar la regresión polinomica con el dataset
from sklearn.preprocessing import PolynomialFeatures
# El valor por defecto de PolynomialFeatures es 2
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# Visualización de los resultados del Modelo Lineal
plt.scatter(X, y, color = "red")
plt.plot(X, lin_reg.predict(X), color = "blue")
plt.title("Modelo de Regresión Lineal")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()


# Visualización de los resultados del Modelo Polinómico
# Crea niveles intermedios
X_grid = np.arange(min(X), max(X), 0.1)
# pasar de vector a matriz
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = "blue")
plt.title("Modelo de Regresión Polinomica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

# Predicción de nuestros modelos
# Se ha añadido la sintaxis de doble corchete necesaria para hacer la predicción en las últimas versiones de Python (3.7+)
lin_reg.predict([[6.5]])
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


