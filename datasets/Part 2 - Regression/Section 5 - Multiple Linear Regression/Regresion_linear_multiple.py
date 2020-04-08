# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:55:32 2020

@author: al_la
"""


# Plantilla de Regresion lineal multiple

# Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# Importar el dataset
dataset = pd.read_csv('50_Startups.csv')
# dataset = dataset[,2:3]

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 4].values


# Codificar datos categóricos
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
# se cambia a 3 
X[:,3] = le_X.fit_transform(X[:,3])


# Codificar con variables dummy
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
# se cambia al 3
onehotencoder = make_column_transformer((OneHotEncoder(), [3]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)

# Evitar la trampa de las variables Dummy,  se debe de eliminar una
X = X[:, 1:]

# En este ejemplo no se categoriza la variable dependiente
le_y = preprocessing.LabelEncoder()
y = le_y.fit_transform(y)


# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Los train y test son los sets que se usarán para entrenar y probar el modelo 
from sklearn.model_selection import train_test_split
# El text_size indica que el 20 por ciento de los datos de X se utilizarán para testear el modelo, normalmente se usa entre 20 y 30 por mucho
# random_state se usa para evitar la aleatoriedad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0)


# No se escalan los datos en este ejemplo
'''
# Escaldo de variables
# Standarización, esto ayuda a que los modeos converjan mas rapidamente
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''
# --------------------------------------
 
# Ajustar el modelo de Regresión lineal multiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Paso 52

# Predicción de los resultados en el conjunto de Testing
y_pred = regression.predict(X_test)

# Paso 53 Eliminación hacia atrás
# Dar un paso hacia atrás, para validar si todas las variables son necesarias.
# COnstruir el modelo ótipo de RLM utilizando la Eliminación hacia atrás

# Paso 53
# Se agrega el vector de 1´s al inicio
import statsmodels.regression.linear_model as sm
# agregar una columna con 1´s y asociarla a nuestro coeficiente del termino independiente.
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)

# Paso 54
# Definir nivel de significación (confianza)
SL = 0.05
# Matriz de caracteristicas óptima
X_opt = X[:, [0,1,2,3,4,5]]
X_opt = np.array(X_opt, dtype=float)
# Realiazar nuevo Regression
# Librería para OLS Ordinary Least Squares
# Se le manda Varable endogena y extrogena
regression_OLS = sm.OLS(endog=y, exog=X_opt).fit()

regression_OLS.summary()
# De inicio se nota que las variables significativas serían const y X2
# Eliminar la varibale predictora con el P-valor más alto, en este caso es X2 y ajustar el nuevo modelo


X_opt = X[:, [0,1,3,4,5]]
X_opt = np.array(X_opt, dtype=float)
regression_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regression_OLS.summary()
# Los resultados muestran que se deberia de eliminar X1
'''
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       5.011e+04   6647.870      7.537      0.000    3.67e+04    6.35e+04
x1           220.1585   2900.536      0.076      0.940   -5621.821    6062.138
x2             0.8060      0.046     17.606      0.000       0.714       0.898
x3            -0.0270      0.052     -0.523      0.604      -0.131       0.077
x4             0.0270      0.017      1.592      0.118      -0.007       0.061  El cero no debería de entrar en el intervalo de confianza
==============================================================================
'''

X_opt = X[:, [0,3,4,5]]
X_opt = np.array(X_opt, dtype=float)
regression_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regression_OLS.summary()

# Paso 55
'''
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       5.012e+04   6572.353      7.626      0.000    3.69e+04    6.34e+04
x1             0.8057      0.045     17.846      0.000       0.715       0.897
x2            -0.0268      0.051     -0.526      0.602      -0.130       0.076
x3             0.0272      0.016      1.655      0.105      -0.006       0.060
==============================================================================
'''

X_opt = X[:, [0,3,5]]
X_opt = np.array(X_opt, dtype=float)
regression_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regression_OLS.summary()

'''
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       4.698e+04   2689.933     17.464      0.000    4.16e+04    5.24e+04
x1             0.7966      0.041     19.266      0.000       0.713       0.880
x2             0.0299      0.016      1.927      0.060      -0.001       0.061
==============================================================================
'''

# Si se elimina X2 se quedaría un modelo de regresion simple, para el ejemplo se va a quitar, pero 
# se revisaran mejores criterios en el futuro
X_opt = X[:, [0,3]]
X_opt = np.array(X_opt, dtype=float)
regression_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regression_OLS.summary()

'''
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       4.903e+04   2537.897     19.320      0.000    4.39e+04    5.41e+04
x1             0.8543      0.029     29.151      0.000       0.795       0.913
==============================================================================
'''



# Eliminación hacia atrás utilizando solamente p-valores:
import statsmodels.formula.api as sm
def backwardElimination(x, sl):    
    numVars = len(x[0])    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        if maxVar > sl:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    x = np.delete(x, j, 1)    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)

# Eliminación hacia atrás utilizando  p-valores y el valor de  R Cuadrado Ajustado:
import statsmodels.formula.api as sm
def backwardElimination(x, SL):    
    numVars = len(x[0])    
    temp = np.zeros((50,6)).astype(int)    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        adjR_before = regressor_OLS.rsquared_adj.astype(float)        
        if maxVar > SL:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    temp[:,j] = x[:, j]                    
                    x = np.delete(x, j, 1)                    
                    tmp_regressor = sm.OLS(y, x.tolist()).fit()                    
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)                    
                    if (adjR_before >= adjR_after):                        
                        x_rollback = np.hstack((x, temp[:,[0,j]]))                        
                        x_rollback = np.delete(x_rollback, j, 1)     
                        print (regressor_OLS.summary())                        
                        return x_rollback                    
                    else:                        
                        continue    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)
