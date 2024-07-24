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