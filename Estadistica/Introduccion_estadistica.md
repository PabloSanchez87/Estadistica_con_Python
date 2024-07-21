# TEMARIO
## Introducción a la Estadística
### Importancia de la estadística en Redes Neuronales
- ¿Por qué es importante?
    - La estadística es **crucial** para la inteleigencia artificial porque **proporciona las herramientas y métodos** necesarios para **analizar datos, construir y validar modelos**, hacer inferencias, manejar la incertidumbre y optimizar algoritmos.
    - **Sin la estadística, muchos de los ancances en IA no serían posibles**

![Aplicaciones de la estadística en IA](/media/AplicacionEstadistica.png)

- **¿Qué es la estadística?**
    - La estadística es una **rama de las matemáticas** que se encarga de **recolectar, analizar, interpretar, presentar y organizar datos**.
    - Es una herramienta fundamental en muchas disciplinas, como la economía, la biología, la ingeniería, la psicología, la sociología, **la inteligencia artificial** y muchas otras, ya que **permite tomar decisiones informadas** basadas en datos y tendencias.

### Estadística descriptiva
- Esta área se enfoca en **describir y resumir un conjunto de datos**.
- Utiliza **medidas** como la media, la mediana, la moda, la desviación estándar, y **gráficos** como histogramas y diagramas de dispersión para representar la información de manera comprensible.

![Estadística descriptiva](/media/descriptiva.png)

#### MEDIDAS DE TENDENCIA
- ¿Qué es la **media**?
    - La media aritmética, es una medida de **tendencia central** que indica el valor promedio de un conjunto de datos.
    - Se utiliza para presentar el valor típico de un conjunto de datos y es una de las medidas más comunes y útiles en la estadística descriptiva.

    ![Estadística descriptiva](/media/media.png)

- ¿Qué es la **mediana**?
    - Es una medida de tendencia central que **representa el valor del medio en un conjunto de datos ordenados**
    - A diferencia de la media, que puede verse afectada por valores extremadamente altos o bajos (*outliers*), **la mediana proporciona una mejor representación del centro de un conjunto de datos asimétricos** o con valores atípicos
    - ¿Cómo se calcula?
        1. Ordeno de menor a mayor la muestra.
        2. Elijo el elemento que se encuentra en el medio.
            - Si el número de elementos de la muestra es **impar** debe tomarse el que ocupe la posicion **(n+1)/2**.
                - 99 --> (99+1)/2 --> 50
            - Si el número de elementos de la muestra es **par** debe tomarse la media de los valores que ocupen la posicion **n/2** y **((n/2)+1)/2**
                - 100 --> 100/2 y ((100/2)+1)/2 --> 50 y 51 --> 50.5

- ¿Qué es la **moda**?
    - La moda en estadística se refiere al valor que aparece con mayor frecuencia en un conjunto de datos.
    - Es simplemente **el número que se repite más a menudo**.
    - La moda es útil porque proporciona una **idea rápida de cuál es el valor más típico** en un conjunto de datos.
    - Sin embargo, a diferencia de la media y la mediana, la moda no representa necesariamente un valor central o típico.

    ![Estadística descriptiva](/media/moda.png)

- [Código de ejemplo: Medidas de tendencia](medidas_de_tendencia.py)

---

#### MEDIDAS DE DISPERSION
- ¿Qué es el **rango**?
  - El rango es una medida de **dispersión** que indica la **diferencia entre el valor máximo y el valor nínimo de un conjunto de datos**.
  - Es una de las formas más sencillas de medir la variabilidad de los datos.
  - ¿Cómo se calcula?
    - Se indica el mayor de los valores **Xmax** de la muestra
    - Se indica el menor de los valores **Xmin** de la muestra
    - La diferencia entre ambos valores es el rango:
      - **Rango = Xmax - Xmin**
  
- ¿Qué es la **varianza**?
  - La varianza es un medida de dispersión que **indica cuánto varían los datos en un conjunto con respecto a la media**.
  - Específicamente, la varianza **mide la media de las diferencias al cuadrado entre cada valor del conjunto y la media del conjunto**.
  ![Varianza](/media/Varianza.png)

- ¿Qué es la **desviación estándar**?
  - La desviación estándar es ina medida de dispersión **que indica cuánto se desvían**, en promedio, **los valores de un conjunto de datos con respecto a su media**.
  - A diferencia de la varianza, la **desviación estándar tiene las mismas unidades** que los daos originales, lo que facilita la interpretación.
    - Una **desviación estándar baja** indica que **los datos están muy dispersos** alrededor de la media.
    - Una **desviación estándar alta** indica que **los datos están más concentrados** cerca de la media.
     
    ![Desviación estándar](/media/desviacion_estandar.png)

- ¿Qué son los **percentiles**?
  - Los percentiles son medidas estadísticas que **dividen un conjunto de datos ordenados en 100 partes iguales**
  - Cada percentil indica **el valor debajo del cual se encuentran un cierto porcentaje de los datos**
  - Por ejemplo, **el percentil 25(P25) es el valor debajo del cual se encuentra el 25% de los datos**, el percentirl 50(P50) es el valor debajo del cual se encuentra el 50% de los datos(**también conocido como la mediana**)
  - ¿Por qué son importantes?
    - **Análisis de distribución**
      - Los percentiles permiten comprender cómo se distribuyen los datos.
      - Por ejemplo, conocer el percentil 90 puede ayudarte a saber qué valor supera el 90% de los datos.
    - **Identificación de valores atípicos**
      - Los percentiles pueden ayudar a identificar valores atípicos o extremos en los datos.
      - Por ejemplo, los valores por debajo del percentil 5 o por encima del percentil 95 pueden considerarse atípicos.

- [Código de ejemplo: Medidas de dispersión](medidas_de_dispersion.py)
  
---

### Estadística inferencial
- Esta área se centra en hacer inferencias o **predicciones** sobre una población **a partir de una muestra de datos**. 
- Utiliza técnicas como la estimación de intervalos de confianza, pruebas de hipótesis, análisis de regresión, y análisis de varianza **para llegar a conclusiones sobre la población de interés**.

## Gráficos y Visualización de Datos
## Probabilidad
## Distribuciones de Probabilidad
## Correlación y Regresión
## Métodos de Muestreo
## Aplicaciones de la Estadística en Redes Neuronales

