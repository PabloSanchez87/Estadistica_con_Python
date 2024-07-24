# Importamos las liberías
import seaborn as sns
import matplotlib.pyplot as plt
import os


# Cargamos los datos de DataSetIris
datos = sns.load_dataset('iris')

# Imprimimos los datos
print(datos)


#! -----------------------------------------------------------------------------------
#? Gráfico de dispersión

# Ruta del archivo de imagen
output_path = "./Estadistica/graficos/grafico_dispersion_iris.png"

if not os.path.exists(output_path):
    sns.scatterplot(data=datos, x='sepal_length', y='sepal_width')
    plt.title('Gráfico de dispersión de LONGITUD del sépalo vs ANCHO')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')

    # Guardamos el gráfico como imagen
    plt.savefig(output_path)

    # Mostramos el gráfico (si es posible, depende donde estés ejecutando el script.)
    plt.show()


#! -----------------------------------------------------------------------------------
#? Gráfico de barras

output_path = "./Estadistica/graficos/grafico_barras_iris.png"

if not os.path.exists(output_path):
    sns.barplot(data=datos, x='species', y='sepal_length')
    plt.title('Gráfico de barras de LONGITUD del sépalo vs Sépalo')
    plt.xlabel('species')
    plt.ylabel('sepal_length')

    # Guardamos el gráfico como imagen
    plt.savefig(output_path)

    # Mostramos el gráfico (si es posible, depende donde estés ejecutando el script.)
    plt.show()


#! -----------------------------------------------------------------------------------
#? Gráfico de histograma

output_path = "./Estadistica/graficos/grafico_histograma_iris.png"

if not os.path.exists(output_path):
    sns.histplot(datos['sepal_length'],bins=10)
    plt.title('Histograma de LONGITUD del sépalo')
    plt.xlabel('sepal_length')
    plt.ylabel('Numero repeticiones')

    # Guardamos el gráfico como imagen
    plt.savefig(output_path)

    # Mostramos el gráfico (si es posible, depende donde estés ejecutando el script.)
    plt.show()


#! -----------------------------------------------------------------------------------
#? Gráfico de violín

output_path = "./Estadistica/graficos/grafico_violin_iris.png"

if not os.path.exists(output_path):
    sns.violinplot(data=datos, x='species', y='sepal_length')
    plt.title('Gráfico de violín')
    plt.xlabel('species')
    plt.ylabel('sepal_length')

    # Guardamos el gráfico como imagen
    plt.savefig(output_path)

    # Mostramos el gráfico (si es posible, depende donde estés ejecutando el script.)
    plt.show()
    
    
#! -----------------------------------------------------------------------------------
#? Gráfico de cajas

# Definir la ruta donde se guardará el gráfico
output_path = "./Estadistica/graficos/grafico_cajas_iris.png"

# Verificar si el gráfico ya existe para evitar sobreescribir
if not os.path.exists(output_path):
    # Crear el gráfico de cajas
    sns.boxplot(data=datos, x='species', y='sepal_length')
    plt.title('Gráfico de cajas de longitud del sépalo por especie')
    plt.xlabel('Species')
    plt.ylabel('Sepal Length')

    # Guardar el gráfico como imagen
    plt.savefig(output_path)

    # Mostrar el gráfico
    plt.show()


#! -----------------------------------------------------------------------------------
#? Heatmap

output_path = "./Estadistica/graficos/grafico_heatmap_iris.png"

if not os.path.exists(output_path):    
    # # Pairplot
    sns.pairplot(data=datos, hue='species')
    plt.show()
    
    #Heatmap
    # Seleccionar solo las columnas numéricas para calcular la matriz de correlación
    correlacion = datos.drop(columns=['species']).corr()
    
    sns.heatmap(correlacion, annot=True, cmap='coolwarm')
    plt.title('Mapa de calor de las correlaciones')

    # Guardamos el gráfico como imagen
    plt.savefig(output_path)

    # Mostramos el gráfico (si es posible, depende donde estés ejecutando el script.)
    plt.show()