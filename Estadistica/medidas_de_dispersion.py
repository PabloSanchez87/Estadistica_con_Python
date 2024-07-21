# Importamos librerias
import pandas as pd
import numpy as np

#! -------------------------------------------------------
# Leemos nuestro dataframe
dataframe = pd.read_csv("Estadistica/salary_data.csv", sep=";") #Revisamos el csv, en esta caso el separador es un ;
# Comprobamos imprimiendo las cabeceras.
print(dataframe.head())

print("·"*40)
#! -------------------------------------------------------
#? Rango con Pandas
rango_pandas = dataframe.income.max() - dataframe.income.min()
print(f"· Rango income con pandas: {rango_pandas}")

#? Rango con Numpy
rango_numpy = np.max(dataframe.age) - np.min(dataframe.age) 
print(f"· Rango age con numpy: {rango_numpy}")

print("·"*40)
#! -------------------------------------------------------
#? Varianza con Pandas
varianza_pandas = dataframe.age.var()
print(f"· Media: {dataframe.age.mean()}")
print(f"· Varianza age con pandas: {varianza_pandas}")
print(f"· Raíz cuadrada de la varianza: {varianza_pandas**0.5}")

print("----")
#? Varianza con numoy
varianza_numpy = np.var(dataframe.age)
print(f"· Media: {np.mean(dataframe.age)}")
print(f"· Varianza age con numpy: {varianza_numpy}")
print(f"· Raíz cuadrada de la varianza: {varianza_numpy**0.5}")

# La varianza da resultado distintos pq pandas y numpy 
# hacen el calculo de forma distinta
# PANDAS
# Calcula la varianza muestral usando n-1 en el denominador.
# Numpy
# Calcula la varianza poblacional usando n en el denominador por defecto.
#? Este comportamiento puede cambiar en NumPy si se especifica el parámetro ddof.
print("----")
varianza_numpy_correcta = np.var(dataframe.age, ddof=1)
print(f"· Varianza age con numpy ajustada: {varianza_numpy_correcta}")
print(f"· Varianza age con pandas: {varianza_pandas}")

# TODO. Nota aclaratoria.
# Varianza Poblacional
# La varianza poblacional se utiliza cuando se tienen todos los datos de la población completa.
# Varianza Muestral
# La varianza muestral se utiliza cuando se tiene una muestra de la población y se desea estimar la varianza de la población.
print("----")
print("VARIANZA POBLACIONAL")
varianza_pandas = dataframe.age.var(ddof=0)
varianza_numpy = np.var(dataframe.age, ddof=0)
print(f"· Varianza age con pandas: {varianza_pandas}")
print(f"· Varianza age con numpy: {varianza_numpy}")
print("----")
print("VARIANZA MUESTRAL")
varianza_pandas = dataframe.age.var(ddof=1)
varianza_numpy = np.var(dataframe.age, ddof=1)
print(f"· Varianza age con pandas: {varianza_pandas}")
print(f"· Varianza age con numpy: {varianza_numpy}")

print("·"*40)
#! -------------------------------------------------------
#? Desviación estándar con PANDAS
desviacion_estandar_pandas = dataframe.age.std()
print(f"· Desviación estándar con pandas: {desviacion_estandar_pandas}")
#? Desviación estándar con NUMPY
desviacion_estandar_numpy = np.std(dataframe.age)
print(f"· Desviación estándar con numpy: {desviacion_estandar_numpy}")

# TODO. Nota aclaratoria.
# Al igual que con la varianza, la desviación estándar en Pandas y Numpy difiere
# por el parámetro "ddof"
# PANDAS 
# Calcula la desviación estándar muestral usando n-1 en el denominador por defecto.
# NUMPY
# Calcula la desviación estandar poblacional usando n en el denominador por defecto.
print("----")
print("DESVIACIÓN ESTÁNDAR POBLACIONAL")
desviacion_estandar_pandas_poblacional = dataframe.age.std(ddof=0)
desviacion_estandar_numpy_poblacional = np.std(dataframe.age, ddof=0)
print(f"· Desviación estándar con pandas: {desviacion_estandar_pandas_poblacional}")
print(f"· Desviación estándar con numpy: {desviacion_estandar_numpy_poblacional}")

print("----")
print("DESVIACIÓN ESTÁNDAR MUESTRAL")
desviacion_estandar_pandas_muestral = dataframe.age.std(ddof=1)
desviacion_estandar_numpy_muestral = np.std(dataframe.age, ddof=1)
print(f"· Desviación estándar con pandas: {desviacion_estandar_pandas_muestral}")
print(f"· Desviación estándar con numpy: {desviacion_estandar_numpy_muestral}")
