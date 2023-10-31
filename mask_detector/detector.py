import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Cargar el modelo previamente entrenado
model = load_model('mask_detector.model')

# Inicializar el detector de caras
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar la cámara (puedes ajustar el número de cámara si es necesario)
cap = cv2.VideoCapture(0)

while True:
    # Capturar un marco de la cámara
    ret, frame = cap.read()

    # Convertir el marco a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el marco
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extraer la región de interés (ROI) que contiene la cara
        roi = frame[y:y + h, x:x + w]
        
        # Redimensionar la ROI para que coincida con el tamaño esperado por el modelo
        roi = cv2.resize(roi, (224, 224))
        roi = np.expand_dims(roi, axis=0)  # Agregar una dimensión de lote

        # Realizar una predicción sobre la ROI
        result = model.predict(roi)

        # Mostrar el resultado en función de la predicción
        if result[0][0] > 0.5:
            cv2.putText(frame, "Con mascarilla", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        else:
            cv2.putText(frame, "Sin mascarilla", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Mostrar el marco con las detecciones
    cv2.imshow('Detección de mascarillas', frame)

    # Detener el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()