import cv2

# Load the Haar Cascade model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture frame from webcam
    ret, frame = cap.read()

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    # Show video frame
    cv2.imshow('Face Detection', frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()
