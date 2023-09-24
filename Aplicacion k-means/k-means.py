# Se importan las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Se Carga el conjunto de datos
iris = pd.read_csv("Dataset/IRIS.csv")
x = iris.iloc[:, [0, 1, 2, 3]].values


# Se encuentra el numero optimo de Clusters utilizando el metodo del codo
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++',
                    max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)


# Luego, entrenamos el modelo K-Means con el número óptimo de clústeres encontrado anteriormente (en este caso, 3).
# fit_predict asigna cada punto de datos a uno de los clústeres.
kmeans = KMeans(n_clusters=3, init='k-means++',
                max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(x)


# Visualización de los Clústeres
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1],
            s=100, c='purple', label='Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1],
            s=100, c='orange', label='Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],
            s=100, c='green', label='Iris-virginica')

# ubicacion media de un clúster de datos
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
            :, 1], s=100, c='red', label='Centroids')

plt.legend()
plt.show()
