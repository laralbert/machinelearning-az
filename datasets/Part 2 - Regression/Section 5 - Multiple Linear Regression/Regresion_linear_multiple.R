
# Plantilla para regresión lineal Multiple

# Importar el dataset 
dataset = read.csv('50_Startups.csv')

# Codificar variables categóricas
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3))


# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Instalar la libreria
install.packages("caTools")
# Cargar la libreria
library(caTools)
# semilla aleatoria
set.seed(123)
# Se hace al revés de python, aquí se declara el porcentaje de entrenamiento
split = sample.split(dataset$Profit,  SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escaldo de variables    no se escala este ejemplo
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Paso 58

# Ajustar el modelo de Regresión lineal multiple con el conjunto de entrenamiento
regressor = lm(formula = Profit ~ . ,
               data = training_set)

summary(regressor)

# 3 estrellas al final significa que es de mucha relevancia la correlacion
# Estudiar el P-valor, R cuadrado ajustado mayor
# R detecta la multicolinealidad por defecto 

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)      4.965e+04  7.637e+03   6.501 1.94e-07 ***
#   R.D.Spend        7.986e-01  5.604e-02  14.251 6.70e-16 ***
#   Administration  -2.942e-02  5.828e-02  -0.505    0.617    
# Marketing.Spend  3.268e-02  2.127e-02   1.537    0.134    
# State2           1.213e+02  3.751e+03   0.032    0.974    
# State3           2.376e+02  4.127e+03   0.058    0.954  

# Paso 59

# Predecir los resultados con el conjunto de testing
y_pred = predict(regressor, newdata = testing_set)

# Paso 69

# Construir un modelo optimo con la eliminación havia atrás
# Ajustar el modelo de Regresión lineal multiple sin las variables
# se le da el conjunto completo para una evaluación más exacta
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State ,
               data = dataset)
summary(regressor)

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)      5.008e+04  6.953e+03   7.204 5.76e-09 ***
#   R.D.Spend        8.060e-01  4.641e-02  17.369  < 2e-16 ***
#   Administration  -2.700e-02  5.223e-02  -0.517    0.608    
# Marketing.Spend  2.698e-02  1.714e-02   1.574    0.123    
# State2           4.189e+01  3.256e+03   0.013    0.990    
# State3           2.407e+02  3.339e+03   0.072    0.943

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend  ,
               data = dataset)
summary(regressor)

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)      5.012e+04  6.572e+03   7.626 1.06e-09 ***
#   R.D.Spend        8.057e-01  4.515e-02  17.846  < 2e-16 ***
#   Administration  -2.682e-02  5.103e-02  -0.526    0.602    
# Marketing.Spend  2.723e-02  1.645e-02   1.655    0.105

regressor = lm(formula = Profit ~ R.D.Spend + Administration ,
               data = dataset)
summary(regressor)

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)     5.489e+04  6.017e+03   9.122  5.7e-12 ***
#   R.D.Spend       8.621e-01  3.016e-02  28.589  < 2e-16 ***
#   Administration -5.300e-02  4.940e-02  -1.073    0.289  

regressor = lm(formula = Profit ~ R.D.Spend ,
               data = dataset)
summary(regressor)

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
#   (Intercept) 4.903e+04  2.538e+03   19.32   <2e-16 ***
#   R.D.Spend   8.543e-01  2.931e-02   29.15   <2e-16 ***
# Multiple R-squared:  0.9465,	Adjusted R-squared:  0.9454 
# El 95% del dato se explica de una forma lineal

# Regresión automática

backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)
