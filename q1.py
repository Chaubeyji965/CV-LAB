import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)


    cv2.imshow('Canny Edge Detection', edges)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
