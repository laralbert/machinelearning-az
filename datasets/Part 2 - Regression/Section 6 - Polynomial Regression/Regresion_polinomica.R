# Regresion Polinómica

# Importar el dataset 
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Instalar l alibreria
# install.packages("caTools")
# Cargar la libreria
# library(caTools)
# semilla aleatoria
set.seed(123)
# Se hace al revés de python, aquí se declara el porcentaje de entrenamiento
# split = sample.split(dataset$Purchased,  SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)


# Escaldo de variables
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# 72
# Ajustar la regresion lineal con el dataset
lin_reg = lm(formula = Salary ~ .,
             data = dataset)
summary(lin_reg)

# Ajustar la regresión polinomica con el dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)
summary(poly_reg)

# Visualización del modelo lineal
ggplot() +
  geom_point(aes(x = dataset$Level, 
                 y = dataset$Salary), 
             colour = "red") +
  geom_line(aes(x = dataset$Level, 
                y = predict(lin_reg, newdata = dataset)),
            colour = "blue") +
  ggtitle("Sueldo vs nivel") +
  xlab("Nivel") +
  ylab("Sueldo (Dolares)")


# Visualización del modelo polinómico
# library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, 
                 y = dataset$Salary), 
             colour = "red") +
  geom_line(aes(x =x_grid, 
                y = predict(poly_reg, newdata = data.frame(Level = x_grid,
                                                           Level2 = x_grid^2,
                                                           Level3 = x_grid^3,
                                                           Level4 = x_grid^4))),
            colour = "blue") +
  ggtitle("Sueldo vs nivel") +
  xlab("Nivel") +
  ylab("Sueldo (Dolares)")

# Predicción de nuevos resultados con regresión lineal
y_pred_lin = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Predicción de nuevos resultados con regresión polinómica
y_pred_poly = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5^2,
                                                Level3 = 6.5^3,
                                                Level4 = 6.5^4))

