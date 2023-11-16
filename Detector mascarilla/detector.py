# USAGE
# python detect_mask_video.py

# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor = 'alenjaircamrgo@gmail.com'
email_password = os.environ.get('qnur uolh tsmo soqd')
email_receptor = 'alenjaircamrgo@gmail.com'
def detect_and_predict_mask(frame, faceNet, maskNet):
	# grab the dimensions of the frame and then construct a blob
	# from it
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()

	# initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the detection
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for
			# the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			if face.any():
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
				face = cv2.resize(face, (224, 224))
				face = img_to_array(face)
				face = preprocess_input(face)

				# add the face and bounding boxes to their respective
				# lists
				faces.append(face)
				locs.append((startX, startY, endX, endY))

	# only make a predictions if at least one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# return a 2-tuple of the face locations and their corresponding
	# locations
	return (locs, preds)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
	default="face_detector",
	help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
	default="mask_detector.model",
	help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector model from disk
print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
print("[INFO] loading face mask detector model...")
maskNet = load_model(args["model"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

contador=0
# loop over the frames from the video stream
# Bucle principal

umbral_alerta=50
tiempo_sin_tapabocas=0
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=800)
    error = False
    # Detecta caras y predice si llevan tapabocas
    (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

    # Itera sobre las caras detectadas
    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        labelValidate = "Con tapabocas" if mask > withoutMask else "Sin tapabocas"
        label = "Con tapabocas" if mask > withoutMask else "Sin tapabocas"
        color = (0, 255, 0) if label == "Con tapabocas" else (0, 0, 255)

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(frame, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

        # Si se detecta a alguien sin tapabocas, incrementa el contador
        # Si el tiempo sin tapabocas supera el umbral, imprime una alerta
        if labelValidate == "Sin tapabocas":
            error = True

    if error:
        tiempo_sin_tapabocas += 1
    else:
        tiempo_sin_tapabocas = 0

    if tiempo_sin_tapabocas > umbral_alerta:
        print("Error  notificacion")
        tiempo_sin_tapabocas = 0 

        subject = "⚠️ Alerta: Persona sin mascarilla detectada"
        body = "Se ha detectado a alguien sin mascarilla. Por favor, tome las medidas necesarias."

        # Guardar la imagen capturada
        nombre_imagen = f"images/alerta_{time.strftime('%Y%m%d%H%M%S')}.jpg"
        cv2.imwrite(nombre_imagen, frame)

        # Crear objeto EmailMessage
        em = EmailMessage()
        em['From'] = email_emisor
        em['To'] = email_receptor
        em['Subject'] = subject
        em.set_content(body)

        # Adjuntar la imagen al correo electrónico
        with open(nombre_imagen, 'rb') as im:
            file_data = im.read()
            file_type = imghdr.what(im.name)
            file_name = im.name
        em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

        # Configurar contexto SSL
        contexto = ssl.create_default_context()

        # Enviar el correo electrónico
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(email_emisor, 'qnur uolh tsmo soqd')
            smtp.sendmail(email_emisor, email_receptor, em.as_string())

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break




cv2.destroyAllWindows()
vs.stop()




