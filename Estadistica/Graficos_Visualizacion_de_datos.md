# [Índice](../README.md)
**1. Introducción a la Estadística Gráficos y Visualización de Datos**  
  - [Introducción estadística](../Estadistica/Introduccion_estadistica.md)
  - [Gráficos y Visualización de datos](../Estadistica/Graficos_Visualizacion_de_datos.md)

**2. Probabilidad**

**3. Distribuciones de Probabilidad**

**4. Correlación y Regresión**

**5. Métodos de Muestreo**

---

## Gráficas y Visualización de datos
### Importancia de la visualización de datos
- ¿Por qué es importante aprender a visualizar datos?
  - La visualización de datos juega un papel crucial tanto en el análisis de datos como en la inteligencia artificial (IA) por varias razones:
    - La visualización ayuda a explorar los datos y entender sus características principales.
      - Mediante gráficos, es posible identificar patrones, tendencias y relaciones entre variables.
    - Los fráficos facilitan la identificación de valores atípicos o anomalías que pueden afectar los resultados de los análisis.
    - Ejemplo de una tabla de datos:
  
      ![Tabla datos](../media/tabladatos.png)

    - Una gráfica nos representa mejor los datos:
      
      ![Gráfica datos](../media/graficadatos.png)

#### ¿Qué es Seaborn?
- `Seaborn` es una **librería de visualización de datos en Python** que se basa en **Matplolib**.
- Proporciona una interfaz de alto nivel para dibujar **gráficos estadísticos atractivos y con estilo**.
- [Página oficial Seaborn](https://seaborn.pydata.org/)
- Seaborn facilita la visualización de datos al ofrecer funciones que permiten crear gráficos complejos con pocas líneas de código.

---

### Tipos de gráficos más comunes

- **Gráfico de dispersión**
  - ¿Qué representan?
    - Muestra la relación entre dos variables continuas mediante puntos en un plano cartesiano, X <-> Y
  - ¿Para qué se usan?
    - Se usa para identificar y analizar relaciones, patrones y tendencias entre dos variables.
  - ¿Qué conclusiones se pueden sacar?
    - Se pueden identificar correlaciones, patrones, tendencias y detectar valores atípicos.
  
    ![Gráfico de dispersión](../media/graficodispersion.png)

---

- **Gráfico de barras**
  - ¿Qué representan?
    - Representan datos categóricos con barras rectangulares, donde la longitud de cada barra es proporcional al valor que representa.
  - ¿Para qué se usan?
    - Se usa para comparar diferentes categorías entre sí.
  - ¿Qué conclusiones se pueden sacar?
    - Permite ver fácilmente las diferencias y comparaciones entre categorías, así como identificar las categorías con valores más altos y más bajos.

    ![Gráfico de barras](../media/graficobarras.png)

---

- **Gráfico de cajas**
  - ¿Qué representan?
    - Rpresentan la distribución de una variable continua mostrando la mediana, los cuartiles y los valores atípicos.
  - ¿Para qué se usan?
    - Se usa para resumir la distribución de datos y detectar valores atípicos.
  - ¿Qué conclusiones se pueden sacar?
    - Se puede ver la mediana, la dispersión, la presencia de valores atípicos, y comparar la distribución entre diferentes grupos.

    ![Gráfico de cajas](../media/graficocajas.png)

---

- **Gráfico de histograma**
  - ¿Qué representan?
    - Muestra la distribución de una variable continua dividiendo el rango de valores en intervalos y contando la frecuencia de los valores en cada intevalo.
  - ¿Para qué se usan?
    - Se usa para entender la distribución y frecuencia de una variable continua
  - ¿Qué conclusiones se pueden sacar?
    - Se puede identificar patrones de distribución, como la simetría, la asimetría, la presencia de múltiples picos(multimodalidad) y detectar valores atípicos.
  
    ![Histograma](../media/histograma.png)

---

- **Gráfico de violín**
  - ¿Qué representan?
    - Combina el blox plot con un gráfico de densidad para mostrar la distribución de una variable continua.
  - ¿Para qué se usan?
    - Se usa para visualizar la distribución y la densidad de una variable, comparando varias categorías o grupos.
  - ¿Qué conclusiones se pueden sacar?
    - Proporciona una visión más detallada de la distribución de los datos, permitiendo comparar la forma de la distribución entre diferentes grupos o categorías.
      
      ![Histograma](../media/graficaviolin.png)

---

- **Gráfico de correlación(Heatmap)**
  - ¿Qué representan?
    - Muestra la relación entre múltiples variables en una matriz, donde los valores son representados con colores.
  - ¿Para qué se usan?  
    - Se usa para identificar y visualizar relaciones y patrones de correlación entre múltiples varibales.
  - ¿Qué conclusiones se pueden sacar?
    - Se puede ver qué variables están altamente correlacionadas positiva o negativamente, lo que es útil para la selección de características y la identificación de relaciones entre variables.
  
    ![Histograma](../media/heatmap.png)

---

### Ejemplos prácticos en Seaborn

> [!IMPORTANT]  
> Es importante conocer los datos con los que vamos a trabajar.

- **Explicación de dataset - DATA SET IRIS**
  - Contiene 150 observaciones de iris (un tipo de flor) de tres especies diferentes:
    - Iris setosa
    - Iris versicolor
    - Iris virginica
  - Cada observación incluye cuatro características medidas de cada flor y la especie a la que pertenece.
  - **Columnas del dataset**
    - **Sepal Length (cm):** 
      - Longitud del sépalo en centímetros.
    - **Sepal Width (cm):** 
      - Ancho del sépalo en centímetros.
    - **Petal Length (cm):** 
      - Longitud del pétalo en centímetros.
    - **Petal Width (cm):** 
      - Ancho del pétalo en centímetros.
    - **Species:** 
      - Especie de la flor, que puede ser una de las tres:
        - setosa
        - versicolor
        - virginica
  
      ![Flor](../media/flor.png)

  - Librerías de Python utilizadas.
  
    ```bash
      pip install matplotlib
    ```

    ```bash
      pip install seaborn
    ```

  - [Código de ejemplo: Data set IRIS](../Estadistica/seaborn_data_set_iris.py)

---
 
### Buenas prácticas de visualización
**1. Claridad y Simplicidad**
- **Evitar la sobrecarga de información:** 
  - Los gráficos deben ser lo más simples posible, evitando elementos innecesarios que puedan distraer o confundir a los espectadores.
- **Usar gráficos adecuados:** 
  - Seleccionar el tipo de gráfico correcto para el tipo de datos y el mensaje que se quiere comunicar. Por ejemplo, usar gráficos de barras para comparaciones discretas y gráficos de líneas para tendencias temporales.
- **Evitar el uso de efectos visuales excesivos:** 
  - Como sombras, gradientes o 3D que no aportan información adicional y pueden complicar la interpretación.

**2. Escalas Apropiadas**
- **Escalas coherentes:** 
  - Asegurarse de que las escalas de los ejes sean coherentes y apropiadas para los datos que se están mostrando. Evitar escalas truncadas que pueden exagerar o minimizar diferencias.
- **Uso de escalas logarítmicas cuando sea necesario:** 
  - Para datos que varían en órdenes de magnitud, una escala logarítmica puede ser más adecuada.
- **Anotar intervalos y unidades:** 
  - Clarificar las unidades de medida y asegurar que los intervalos en los ejes sean uniformes y comprensibles.
  
**3. Colores y Etiquetas**
- **Uso consciente del color:** 
  - Utilizar colores que sean accesibles para todos, incluyendo a las personas con daltonismo. Evitar el uso excesivo de colores y asegurarse de que cada color tenga un propósito claro.
- **Contraste adecuado:** 
  - Asegurar un buen contraste entre el texto, las líneas y el fondo para que la información sea legible.
- **Etiquetas claras y legibles:** 
  - Todas las partes del gráfico deben estar claramente etiquetadas, incluyendo los ejes, las leyendas y los puntos de datos, si es relevante.
  
**4. Narrativas y Contexto**
- **Proveer contexto:** 
  - Asegurar que el gráfico incluya suficiente contexto para que el espectador entienda lo que se está viendo. Esto puede incluir títulos descriptivos, subtítulos, notas al pie o referencias.
- **Narrativa clara:** 
  - El gráfico debe contar una historia clara o transmitir un mensaje específico. Esto puede lograrse destacando ciertos datos o anotando puntos importantes directamente en el gráfico.
- **Mantener la precisión:** 
  - Asegurar que el gráfico represente los datos con precisión, sin distorsionar la realidad. Es importante no manipular gráficos para hacer que los datos parezcan más impresionantes o significativos de lo que realmente son.

- **Ejemplos y Consideraciones Adicionales:**
  
  - **Análisis de audiencias:** 
    - Considerar quién es el público objetivo y adaptar la visualización en consecuencia.
  - **Pruebas de interpretación:** 
    - Antes de compartir el gráfico, pedir a alguien más que lo interprete para asegurarse de que el mensaje es claro.
  - **Documentación:** 
    - Incluir fuentes de datos, métodos de análisis, y cualquier otra información relevante que ayude a contextualizar el gráfico y respaldar su credibilidad.

---

### Limitaciones y preocupaciones al usar gráficos

> [!IMPORTANT]
> Los gráficos son herramientas muy potentes para explicar las diferentes realidades. Sin embrago, también estos tienen limitaciones.

- **Sesgo y manipulación**
  - **Selección de datos**
    - Seleccionar solo ciertos datos para incluir en un gráfico puede llevar a intepretaciones engañosas. 
    - Es importante ser transparente sobre qué datos se están incluyendo y por qué.
  - **Manipulación del Eje Y**
    - Cambiar la escala del eje Y puede exagerar o miminizar las diferencias aparentes en los datos. 
    - Siempre muestra los ejes claramente y considera empezar los ejes en cero cuando sea posible.
  - **Gráficos 3D y Perpectiva**
    - Los gráficos en 3D pueden ser visualmente atracticos pero a menudo distorsionan la interpretación de los datos.
    - La perspectica puede hacer que los datos sean difíciles de leer con precisión.

- **Precisión**
  - **Muestreo insuficiente**
    - Si los datos representados en un gráfico provienen de un muestreo insuficiente, las conclusiones pueden no ser fiables.
    - Asegúrate de que los datos sean representativos.
  - **Agregación de datos**
    - La agregación de datos puede ocultar variaciones importantes.
    - Mostrar promedios sin desviaciones estándar o rangos puede dar una visión incompleta de los datos.
  - **Errores de muestreo y representación**
    - Los gráficos deben tener en cuenta los errores de muestreo y representación.
    - Incluye imágenes de error cuando sea necesario y sé transparente sobre las limitaciones de los datos.

- **Contexto y comparaciones inadecuadas**
  - **Falta de contexto**
    - Los gráficos que no proporcionan suficiente contexto pueden llevar a interprestaciones erróneas.
    - Asegúrate de que los espectadores comprendan de dónde vienen los datos y en qué contexto deben ser interpretados.
  - **Comparaciones inadecuadas**
    - Comparar datos que no son comparables puede llevar a conluciones erróneas.
    - Asegúrate de que las comparaciones sean válidas y estén bien fundamentadas.





































