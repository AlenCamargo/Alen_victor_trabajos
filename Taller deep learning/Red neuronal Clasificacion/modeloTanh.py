import tensorflow as tf
from tensorflow import keras

datos_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
etiquetas = [0, 1, 1, 0]

modelo_tanh = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    keras.layers.Dense(8, activation='tanh'),  # Capa oculta 1
    keras.layers.Dense(8, activation='tanh'),  # Capa oculta 2
    keras.layers.Dense(8, activation='tanh'),  # Capa oculta 3
    keras.layers.Dense(8, activation='tanh'),  # Capa oculta 4
    keras.layers.Dense(8, activation='tanh'),  # Capa oculta 5
    keras.layers.Dense(1, activation='sigmoid'),
])

# Compilar y entrenar el modelo
modelo_tanh.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


modelo_tanh.fit(datos_entrada, etiquetas, epochs=1000, verbose=0)


loss_tanh, accuracy_tanh = modelo_tanh.evaluate(datos_entrada, etiquetas)


predictions_tanh = modelo_tanh.predict(datos_entrada)

print("Modelo con Tanh - Precisión:", accuracy_tanh)
print("Predicciones con Tanh:\n", predictions_tanh)
