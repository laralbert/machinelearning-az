# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:56:51 2020

@author: al_la
"""


# Plantilla de SVR

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""

# Escalado de variables
# El SVR si requiere el escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1, 1))

# Ajustar la regresión con el dataset
# Crear aquí nuestro modelo de regresión
from sklearn.svm import SVR
regression = SVR(kernel = "rbf")
regression.fit(X, y)


# Predicción de nuestros modelos
# Equivalentes
# Predicción escalando el valor a buscar
y_pred = regression.predict(sc_X.transform(np.array(6.5).reshape(1, -1)))
y_pred = regression.predict(sc_X.transform([[6.5]]))
# Revertir el escalado de la predicción
y_pred = sc_y.inverse_transform(y_pred)
# Predicción para más de una busqueda
y_pred = sc_y.inverse_transform(regression.predict(sc_X.transform(np.array([[6.5],[7]]))))

# Visualización de los resultados del Modelo Polinómico
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regression.predict(X_grid), color = "blue")
plt.title("Modelo de Regresión (SVR)")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()



