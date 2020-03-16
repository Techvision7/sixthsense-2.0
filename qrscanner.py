import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import imutils
import datetime

def qrscannner():
	font = cv2.FONT_HERSHEY_SIMPLEX
	cap = cv2.VideoCapture(0)
	while True:
		ret, frame = cap.read()
		#frame = imutils.resize(frame, width=400)
		#find barcodes in the frame and decode each of the barecode and qr code
		barcodes = pyzbar.decode(frame)
		for barcode in barcodes:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
			barcodeData = barcodde.data.decode("utf-8")
			barcodetype = barcode.type

			text = "{} ({})".format(barcodeData, barcodetype)
			cv2.putText(frame, text,(x,y-10), font, 0.5, (255,0,0))

		cv2.imshow("barcode", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break
	cap.release()		
	cv2.destroyAllwindows()
	cap.release()

qrscannner()
