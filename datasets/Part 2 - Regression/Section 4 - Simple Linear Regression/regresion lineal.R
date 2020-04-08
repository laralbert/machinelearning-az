# Regresion Lineal SImple

# Importar el dataset 
dataset = read.csv('Salary_Data.csv')

# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Instalar l alibreria
# install.packages("caTools")
# Cargar la libreria
library(caTools)
# semilla aleatoria
set.seed(123)
# Se hace al revés de python, aquí se declara el porcentaje de entrenamiento
split = sample.split(dataset$Salary,  SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escaldo de variables
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de regresion lineal simple con el conjunto de entrenamiento
# La tilde significa en "relacion a "
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# Usar en terminal  summary(regressor)
# 3 estrellas al final significa que es de mucha relevancia la correlacion
# Estudiar el P-valor, R cuadrado ajustado mayor

# Predecir resultados con el conjunto testing
# Los nombres de las columnas deben de ser iguales
y_pred = predict(regressor, newdata = testing_set)

# Visualización de los resultados en el conjunto de entrenamiento  : ggplot2 parte de Tydiverse
install.packages("ggplot2")
library(ggplot2)

# Graficar los datos del conjunto de entrenamiento
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, 
                 y = training_set$Salary), 
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Suledo vs años de experiencia (Conjunto de entrenamiento)") +
  xlab("Años de experiencia") +
  ylab("Sueldo (Dolares)")

# Graficar los datos del conjunto de testing
ggplot() +
  geom_point(aes(x = testing_set$YearsExperience, 
                 y = testing_set$Salary), 
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Suledo vs años de experiencia (Conjunto de testing)") +
  xlab("Años de experiencia") +
  ylab("Sueldo (Dolares)")

