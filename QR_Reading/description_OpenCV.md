# Drone QR Scanner

A real-time QR code detection system designed for drone applications using OpenCV and computer vision. This application captures video feed from a camera source (webcam or drone stream) and automatically detects and decodes QR codes in the video stream.

## Repository Information

- **Repository**: https://github.com/SauravBhowmick/QR_Generator_Reader
- **File Location**: `QR_Reading/QR_Reader.py`
- **Main Branch**: `main`

## Features

- **Real-time QR Code Detection**: Automatically detects and decodes QR codes from live video feed
- **Visual Feedback**: Draws green bounding boxes around detected QR codes
- **Flexible Input Sources**: Supports both webcam and drone video streams
- **Drone-Ready**: Easily configurable for RTSP streams or drone SDK integration
- **Lightweight**: Minimal dependencies and efficient processing

## Prerequisites

- Python 3.6 or higher
- OpenCV (cv2) library
- Camera/webcam or drone with video streaming capability

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SauravBhowmick/QR_Generator_Reader.git
   cd QR_Generator_Reader/QR_Reading
   ```

2. **Install required dependencies**
   ```bash
   pip install opencv-python
   ```

   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage (Webcam)

Run the script with default settings to use your computer's webcam:

```bash
python QR_Reader.py
```

### Drone Integration

For drone applications, modify the video capture source in the code:

```python
# Replace this line:
cap = cv2.VideoCapture(0)

# With your drone's RTSP stream URL:
cap = cv2.VideoCapture("rtsp://drone_ip:port/stream")

# Or with drone SDK specific stream initialization
```

### Controls

- **ESC or 'q'**: Quit the application
- The application will automatically detect and display QR codes in real-time

## Configuration

### Camera Sources

- **Default webcam**: `cv2.VideoCapture(0)`
- **External camera**: `cv2.VideoCapture(1)` (increment number for additional cameras)
- **RTSP stream**: `cv2.VideoCapture("rtsp://ip:port/path")`
- **HTTP stream**: `cv2.VideoCapture("http://ip:port/stream")`

### Drone-Specific Configuration

Popular drone platforms and their typical stream configurations:

**DJI Drones:**
```python
# Using DJI Mobile SDK or similar
cap = cv2.VideoCapture("rtsp://192.168.1.1:8080/live")
```

**Custom Drones:**
```python
# Replace with your drone's specific stream URL
cap = cv2.VideoCapture("rtsp://drone_ip:1935/live/stream")
```

## Code Structure

```
QR_Generator_Reader/
├── QR_Reading/
│   ├── QR_Reader.py       # Main QR reading application
│   └── README.md          # This documentation
```

## How It Works

1. **Video Capture**: Initializes video capture from specified source (webcam/drone)
2. **Frame Processing**: Continuously reads frames from the video stream
3. **QR Detection**: Uses OpenCV's built-in QR code detector to scan each frame
4. **Data Extraction**: Decodes QR code data when detected
5. **Visual Feedback**: Draws green bounding rectangles around detected QR codes
6. **Output**: Prints decoded QR code data to console

## Output

When a QR code is detected, the application will:
- Print the decoded data to the console: `QR Code detected: [decoded_content]`
- Draw a green rectangle around the QR code in the video feed
- Continue scanning for additional QR codes

## Troubleshooting

### Common Issues

**Camera not found:**
```
Failed to grab frame
```
- Check camera connection
- Verify camera index (try 0, 1, 2, etc.)
- Ensure camera is not being used by another application

**Poor QR code detection:**
- Ensure good lighting conditions
- Check QR code size (not too small or too large)
- Maintain stable camera position
- Clean camera lens

**Drone connection issues:**
- Verify drone IP address and port
- Check network connectivity
- Ensure drone is broadcasting video stream
- Confirm RTSP/HTTP stream URL format

### Performance Optimization

For better performance on resource-constrained systems:

```python
# Reduce frame size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Adjust frame rate
cap.set(cv2.CAP_PROP_FPS, 15)
```

## Advanced Features

### Multiple QR Code Detection

The current implementation detects one QR code at a time. For multiple QR codes:

```python
# Use detectAndDecodeMulti for multiple QR codes
success, data_list, points_list, _ = detector.detectAndDecodeMulti(frame)
```

### Data Logging

Add logging functionality to save detected QR codes:

```python
import datetime

if data:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("qr_log.txt", "a") as f:
        f.write(f"{timestamp}: {data}\n")
```

## Dependencies

- **OpenCV (cv2)**: Computer vision library for video processing and QR code detection
- **NumPy**: Array processing (included with OpenCV)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV community for computer vision tools
- Contributors to QR code detection algorithms
- Drone development communities for integration insights

## Support

For support, questions, or feature requests:
- Open an issue on GitHub
- Contact: [bhowmicksaurav28@gmail.com]

---

**Note**: This application is designed for educational and development purposes. Ensure compliance with local regulations when using drones and camera systems.
