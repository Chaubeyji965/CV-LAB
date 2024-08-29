import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for segmentation (e.g., red color)
    lower_bound = np.array([150, 0, 140])
    upper_bound = np.array([255, 85, 255])

    # Create a mask for the color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    color_segmented = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the result
    cv2.imshow('Color-Based Segmentation', color_segmented)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
1