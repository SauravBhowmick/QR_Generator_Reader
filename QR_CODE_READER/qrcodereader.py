import cv2
from pyzbar.pyzbar import decode

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Decode QR codes in the frame
    codes = decode(frame)

    for code in codes:
        data = code.data.decode('utf-8')
        print("QR Code:", data)

        # GREEN BOX AROUND THE QR CODE
        x, y, w, h = code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show the frame with box for 2 seconds
        cv2.imshow("QR Scanner", frame)
        cv2.waitKey(2000)

        # Exit after showing
        cap.release()
        cv2.destroyAllWindows()
        exit()

    # Show live feed
    cv2.imshow("QR Scanner", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
