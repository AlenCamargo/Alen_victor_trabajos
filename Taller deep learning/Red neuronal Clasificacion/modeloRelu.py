import tensorflow as tf
from tensorflow import keras

datos_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
etiquetas = [0, 1, 1, 0]

modelo = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    keras.layers.Dense(4, activation='relu'),  # Capa oculta 1
    keras.layers.Dense(4, activation='relu'),  # Capa oculta 2
    keras.layers.Dense(4, activation='relu'),  # Capa oculta 3
    keras.layers.Dense(4, activation='relu'),  # Capa oculta 4
    keras.layers.Dense(4, activation='relu'),  # Capa oculta 5
    keras.layers.Dense(1, activation='sigmoid'),
])

# Ejecutar el modelo
modelo.compile(optimizer='adam',
               loss='binary_crossentropy',
               metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(datos_entrada, etiquetas, epochs=1000, verbose=0)

# Evaluar el modelo
loss, accuracy = modelo.evaluate(datos_entrada, etiquetas)

# Hacer predicciones
predictions = modelo.predict(datos_entrada)
print(predictions)
