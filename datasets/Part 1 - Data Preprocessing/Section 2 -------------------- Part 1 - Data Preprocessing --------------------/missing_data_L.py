# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:24:29 2020

@author: al_la
"""


# Plantilla de preprocesado

# Como importar las datos NA
import numpy as np
import matplotlib.pyplot as plt    
import pandas as pd        

# Importar el dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[: , 3].values

# Tratamiento de los nan
from sklearn.impute import SimpleImputer
# reemplazar por medias
imputer = SimpleImputer(strategy = "mean")
# medias en columns 1 y 2, la 0 no es numérica
imputer = imputer.fit(X[: , 1:3])
# Cambiar valores por dichas medias
X[:, 1:3] = imputer.transform(X[:, 1:3])