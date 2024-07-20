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