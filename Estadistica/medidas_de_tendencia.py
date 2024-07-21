""" 
Dataset de trabajo

El conjunto de datos contien un informe salarial fabricado sobre el que se pueden realizar análisis para intentar estimar el salario en función de las condiciones dadas.
Hoy 100000 puntos de datos, 50000 de ellos son mujeres y otros 50000 son hombres

Enlace a dataset.
https://www.kaggle.com/datasets/micheldc55/anual-salary-reports-survey
    - ID
    - Ingresos
    - Edad
    - Sexo/Género
    - Nivel de estudios
"""
# Forma básica para calcular Media, moda y mediana.
def media_manual(vector):
    # Media
    suma = 0
    n_elementos = 0
    
    for elemento in vector:
        suma += elemento
        n_elementos += 1
    
    media = (1/n_elementos)*suma
    print(f'· Media con bucle: {media}')
 
def media_metodo(vector):
    # Cálculo de la media usando otros alternativas en Python
    suma = sum(vector)
    n_elementos=len(vector)
    
    media = (1/n_elementos)*suma
    print(f'· Media con sum y len: {media}')

def moda_manual(vector):
    moda = 0
    repeticiones = 0
    
    dic = {}
    
    for elemento in vector:
        if not dic.get(elemento):
            dic[elemento] = 1
        else:
            dic[elemento] += 1
            
        if dic[elemento] > repeticiones:
            moda = elemento
    
    print(f'· Moda con bucle: {moda}') 
    
def mediana_manual(vector:list):
    vector.sort(reverse=False) # Ordenar de menor a mayor.
    punto_medio = int(len(vector)/2)
    
    if len(vector) % 2 == 0:
        mediana = (vector[punto_medio] + vector[punto_medio])/2
    else:
        mediana = vector[punto_medio]
    
    print(f'· Mediana con bucle: {mediana}')

# Prueba
vector =[1,2,3,4,5,6,7,8,9,8,6,5,7,5]
media_manual(vector)
media_metodo(vector)
moda_manual(vector)
mediana_manual(vector)

print("·"*40)

#######################################################
# Importamos las herramientas de Data Science
import pandas as pd
import numpy as np

#? VERSIÓN PANDAS
# Leemos nuestro dataframe
dataframe = pd.read_csv("Estadistica/salary_data.csv", sep=";") #Revisamos el csv, en esta caso el separador es un ;

# Comprobamos imprimiendo las cabeceras.
print(dataframe.head())

print("·"*40)

# Media
print(f"· Media: {dataframe.age.mean()}") 
# Moda
print(f"· Moda: {dataframe.age.mode()}") 
# Mediana
print(f"· Mediana: {dataframe.age.median()}") 

print("·"*40)


#? VERSIÓN NUMPY 
# Recomendación: Trabajar con numpy arrays en vez de dataframe.

array = np.array(dataframe.age)

# Media
print(f"· Media: {np.mean(array)}") 

# Moda
    # Numpy no tiene herramientas para calcular la moda.
    # Opción:
    
# np.unique(array, return_counts=True) devuelve los valores únicos en array y sus respectivas frecuencias.
values, counts = np.unique(array, return_counts=True) 
# np.argmax(counts) encuentra el índice del valor más frecuente.
# values[np.argmax(counts)] devuelve el valor de la moda.
mode_value = values[np.argmax(counts)]
print(f"· Moda: {mode_value}")

# Mediana
print(f"· Mediana: {np.median(array)}")


