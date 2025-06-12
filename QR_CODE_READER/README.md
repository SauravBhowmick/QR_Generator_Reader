
# 📷 QR Code Scanner Using OpenCV and Pyzbar (Beginner Project)

This is a simple Python project that opens your webcam, scans for QR codes in real-time, and draws a green box around any QR code it detects. When a QR code is found, the scanner prints the data and exits.

---

## 🧠 What will Learn

- How to access a webcam using OpenCV (`cv2`)
- How to scan QR codes in live video using `pyzbar`
- How to draw boxes using OpenCV
- Basic Python control flow and OpenCV window management

---

## 🚀 Features

✅ Real-time QR code scanning via webcam  
✅ Green box drawn around the QR code  
✅ QR content is printed in the terminal  
✅ Automatic exit after reading first QR code  
✅ Press 'q' anytime to manually quit  

---

## 📦 Requirements

Install Python libraries before running:

```bash
pip install opencv-python pyzbar

## ▶️ How to Run

Make sure your webcam is connected and working.

Then:
1. Hold a QR code in front of the webcam.
2. A green box will appear around it.
3. QR content will be printed in the terminal.
4. Program exits after detection (or press 'q' to quit manually).

## 🛠️ Future Improvements

- ✅ **Display QR code text on the video screen** instead of only printing in terminal
- 🔁 **Keep scanning continuously** instead of exiting after the first QR code
- 💾 **Save scanned QR data to a text file** for later use
- 🖼️ **Scan QR codes from images** (not just webcam)
- 🔔 **Play a sound/beep** when a QR code is detected
- 🧠 **Add barcode support** in addition to QR codes

---

## 🙌 Author

Made with ❤️ by [Amit Kumar](https://github.com/1Amitkry)

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
