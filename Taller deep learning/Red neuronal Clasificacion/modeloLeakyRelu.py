import tensorflow as tf
from tensorflow import keras

datos_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
etiquetas = [0, 1, 1, 0]

modelo_leaky_relu = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    # Capa oculta 1 con Leaky ReLU
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    # Capa oculta 2 con Leaky ReLU
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    # Capa oculta 3 con Leaky ReLU
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    # Capa oculta 4 con Leaky ReLU
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    # Capa oculta 5 con Leaky ReLU
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    keras.layers.Dense(1, activation='sigmoid'),
])

# Compilar y entrenar el modelo
modelo_leaky_relu.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
modelo_leaky_relu.fit(datos_entrada, etiquetas, epochs=1000, verbose=0)
loss_leaky_relu, accuracy_leaky_relu = modelo_leaky_relu.evaluate(
    datos_entrada, etiquetas)
predictions_leaky_relu = modelo_leaky_relu.predict(datos_entrada)
print("Modelo con Leaky ReLU - Precisión:", accuracy_leaky_relu)
print("Predicciones con Leaky ReLU:\n", predictions_leaky_relu)
