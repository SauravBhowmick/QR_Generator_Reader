# QR_Generator_Reader

## Generator
A Python library that converts product information into scannable QR codes for retail, e-commerce, and inventory management. Input product details like name, price, description, SKU, and manufacturer to generate professional QR codes in JSON, text, or URL formats. Perfect for product packaging, inventory tracking, customer information sharing, and mobile applications. Features customizable styling, error correction, and easy integration. Supports both individual products and batch processing. Ideal for businesses wanting to bridge physical products with digital information through mobile-friendly QR code scanning.

## Reader
This Python script uses OpenCV to capture video from a webcam (or drone camera) and detect QR codes in real time. It initializes a video stream, scans each frame using cv2.QRCodeDetector(), and if a QR code is found, it decodes the data and draws a green bounding box around it. The live video feed is displayed in a window, and the program exits when the user presses the q key.
