import cv2

# Initialize camera (0 = default webcam; change if drone has a specific stream URL)
cap = cv2.VideoCapture(0)  # For drone feed, replace with RTSP URL or drone SDK stream

# QR code detector
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    data, points, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code detected:", data)

        if points is not None:
            points = points[0].astype(int)
            for i in range(len(points)):
                pt1 = tuple(points[i])
                pt2 = tuple(points[(i + 1) % len(points)])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Drone QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
