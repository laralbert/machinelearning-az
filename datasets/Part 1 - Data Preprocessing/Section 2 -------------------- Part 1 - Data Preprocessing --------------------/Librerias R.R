# Plantilla para el preprocesado de datos

# Importar el dataset 
dataset = read.csv('Data.csv')

# Tratamiento de los valores N/A
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)

# Codificar variables categóricas
dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No","Yes"),
                           labels = c(0,1))

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
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])










