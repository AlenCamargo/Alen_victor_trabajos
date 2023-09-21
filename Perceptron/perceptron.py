
# Se importan bibliotecas necesarias

# biblioteca utilizada para la manipulacion de matrices
import numpy as np

# biblioteca que permite visualizar graficos
import matplotlib.pyplot as plt


# funciones proporcionadas por la biblioteca scikit-learn (sklearn) para generar datos de muestra y dividir datos en conjuntos de entrenamiento y prueba
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# Clase para el Perceptrón


class PerceptronClassifier:
    def __init__(self, learning_rate=0.1, max_iterations=50, random_seed=1):
        # Tasa de aprendizaje (entre 0.0 y 1.0)
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations  # Número de iteraciones
        self.random_seed = random_seed  # Semilla para números aleatorios
  # funcion para entrenar el perceptron

    def fit(self, X, y):
        # Inicialización de pesos con valores pequeños aleatorios
        np.random.seed(self.random_seed)
        self.weights = np.random.normal(
            loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []  # Lista para almacenar errores por época

        for _ in range(self.max_iterations):
            errors = 0
            for xi, target in zip(X, y):
                # Actualización de pesos basada en el error
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                errors += int(update != 0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        # Cálculo de la entrada neta
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        # Predicción de clase después del paso unitario
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Función para calcular la distancia de Minkowski entre dos puntos


def minkowski_distance(x1, x2, p):
    return (np.sum((x1 - x2) ** p)) ** (1 / p)

# Clase para el clasificador k-Nearest Neighbors (k-NN)


class KNearestNeighborsClassifier:
    def __init__(self, n_neighbors, p=2):
        self.n_neighbors = n_neighbors  # Número de vecinos a considerar
        self.p = p  # Parámetro de distancia de Minkowski (2 para euclidiana)

    def predict(self, X_train, y_train, X_test):
        y_pred = []
        for x_test in X_test:
            # Calcular distancias entre el punto de prueba y los puntos de entrenamiento
            distances = [minkowski_distance(
                x_test, x_train, self.p) for x_train in X_train]

            # Combinar etiquetas de entrenamiento y distancias en un conjunto de datos
            dataset = np.column_stack((y_train, distances))

            # Ordenar el conjunto de datos por distancia
            dataset = dataset[dataset[:, 1].argsort()]

            # Tomar los k vecinos más cercanos
            k_nearest = dataset[:self.n_neighbors]

            # Realizar un voto mayoritario entre los k vecinos
            unique, counts = np.unique(k_nearest[:, 0], return_counts=True)
            predicted_label = unique[np.argmax(counts)]
            y_pred.append(predicted_label)
        return np.array(y_pred)


def main():
    n_clusters = 3

    # Generar datos de muestra con tres clases
    X, y_true = make_blobs(n_samples=200, centers=n_clusters,
                           cluster_std=1.2, random_state=3)

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_true, test_size=0.25, random_state=1)

    # Crear una instancia del Perceptrón y entrenarlo
    perceptron = PerceptronClassifier(learning_rate=0.5, max_iterations=5)
    perceptron.fit(X_train, y_train)

    # Realizar predicciones con el Perceptrón
    y_pred_perceptron = perceptron.predict(X_test)

    # Crear una instancia del k-NN y realizar predicciones
    knn = KNearestNeighborsClassifier(n_neighbors=5)
    y_pred_knn = knn.predict(X_train, y_train, X_test)

    # Visualizar los resultados
    plt.style.use('classic')
    plt.scatter(X_train[:, 0], X_train[:, 1], s=100, c=y_train)
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_knn,
                s=100, marker='*', label='k-NN Predictions')
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_perceptron,
                s=100, marker='x', label='Perceptron Predictions')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    main()
