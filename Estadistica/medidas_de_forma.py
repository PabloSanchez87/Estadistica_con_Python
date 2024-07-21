import pandas as pd
import numpy as np
from scipy.stats import skew


#! -------------------------------------------------------
# Leemos nuestro dataframe
dataframe = pd.read_csv("Estadistica/salary_data.csv", sep=";") #Revisamos el csv, en esta caso el separador es un ;
# Comprobamos imprimiendo las cabeceras.
print(dataframe.head())

print("·"*40)

# Definir la función para generar datos de una distribución normal y calcular la curtosis
def normal_dist():
    # Parámetros de la distribución normal
    media = 0
    desviacion_estandar = 1
    tamaño = 100000
    # Generar datos aleatorios con distribución normal
    datos = np.random.normal(loc=media, scale=desviacion_estandar, size=tamaño)
    data=pd.Series(datos)

    # Calcular y mostrar la curtosis bruta
    print(f"· Curtosis distribución normal bruta: {data.kurtosis()}")


#! -------------------------------------------------------

#? Calculo ASIMETRIA
# Calculo de Asimetría (Skewness)
asimetria_pandas=dataframe.income.skew()
print(f'· Asimetria de Salarios con Pandas {asimetria_pandas}')

# Es decir, la asimetria es positiva, es decir la mayoria de salarios se encuentran en la parte izquierda, 
# es decir hay más salarios bajos que altos
# Numpy no tiene esa funcion por lo que podriamos utilzar otra libreria de datascience Scipy

asimetria_scipy=skew(dataframe.age)
print(f'· Asimetria de Salarios con Scipy {asimetria_scipy}')
#Es decir, la asimetria es positiva, es decir la mayoria de las personas se encuentran en la parte izquierda, son mayores que la media

print("----")
#? Calculo Curtosis
curtosis = dataframe.income.kurtosis()  # curtosis = dataframe['income'].kurtosis()
print(f'· Curtosis de ingresos (excesiva): {curtosis}') # Imprime la curtosis excesiva (sin restar 3).

# Calculo curtosis de la distribución normal para ver si se le resta 3 o vale 0
normal_dist()

#TODO Nota aclarativa.
# Curtosis
# Curtosis positiva (> 0): 
#   Indica una distribución con colas más pesadas que la normal (más puntos en los extremos).
# Curtosis negativa (< 0): 
#   Indica una distribución con colas más ligeras que la normal (menos puntos en los extremos).
# Curtosis igual a 0: 
#   Indica que la distribución tiene una forma similar a la distribución normal en términos de colas.

# Curtosis Excesiva
# A menudo, la curtosis se compara con la curtosis de una distribución normal para entender 
#   si es "más pesada" o "menos pesada". La curtosis de una distribución normal es 3, 
#   pero a menudo se usa la curtosis excesiva, que se define como:
#           Curtosis excesiva = curtosis - 3
#   Curtosis excesiva > 0: 
#       La distribución tiene colas más pesadas que la normal.
#   Curtosis excesiva < 0: 
#       La distribución tiene colas más ligeras que la normal.
#   Curtosis excesiva = 0: 
#       La distribución tiene colas similares a la normal.