# Plantilla para el preprocesado de datos

# Importar el dataset 
dataset = read.csv('Data.csv')
# dataset = dataset[, 2:3]

# Dividir el dataset en connjunto de entrenamiento y conjunto de testing
# Instalar l alibreria
install.packages("caTools")
# Cargar la libreria
library(caTools)
# semilla aleatoria
set.seed(123)
# Se hace al revés de python, aquí se declara el porcentaje de entrenamiento
split = sample.split(dataset$Purchased,  SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)


# Escaldo de variables
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])


 





