import cv2 
import numpy as np 
import pyautogui 

low_pink = np.array([140, 50, 50])  
high_pink = np.array([170, 255, 255])

cap = cv2.VideoCapture(0) 

prev_y = 0

while True: 
	ret, frame = cap.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	mask = cv2.inRange(hsv, low_pink, high_pink) 
	contours, hierarchy = cv2.findContours( 
		mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

	for i in contours: 
		area = cv2.contourArea(i) 
		if area > 1000: 
			x, y, w, h = cv2.boundingRect(i) 
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
			if y < prev_y: 
				pyautogui.press('capslock') 
			prev_y = y 
	cv2.imshow('frame', frame) 
	if cv2.waitKey(1) == ord('q'): 
		break

cap.release() 
cap.closeAllWindow() 


