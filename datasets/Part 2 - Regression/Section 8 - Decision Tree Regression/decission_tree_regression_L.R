# Plantilla de arbol de regresión

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)


# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar Modelo de Regresión con el Conjunto de Datos
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

# Predicción de nuevos resultados con Árbol de Regresión 
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# Visualización del Árbol de regresión
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression, 
                                        newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Prediccion (Modelo de Arbol de Regresion)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")


x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Prediccion (Modelo de Arbol de Regresion)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")