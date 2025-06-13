# 📷 Enhanced QR Code Scanner

A comprehensive real-time QR code detection system that combines the best features from multiple approaches. This application supports both webcam and drone applications using OpenCV and pyzbar for maximum compatibility and performance.

## 🌟 Features

✅ **Dual Detection Methods**: Uses both pyzbar and OpenCV's built-in QR detector for maximum reliability  
✅ **Real-time Scanning**: Live video feed processing from webcam or drone streams  
✅ **Visual Feedback**: Green bounding boxes and polygon outlines around detected QR codes  
✅ **Flexible Operation Modes**: Single detection or continuous scanning  
✅ **Multiple Input Sources**: Webcam, external cameras, RTSP streams, HTTP streams  
✅ **Data Logging**: Optional logging of detected QR codes with timestamps  
✅ **On-Screen Display**: QR code content displayed directly on video feed  
✅ **Frame Capture**: Save frames with 's' key  
✅ **Pause/Resume**: Control scanning with 'p' key  
✅ **Drone-Ready**: Optimized for drone video streams and applications  
✅ **Cross-Platform**: Works on Windows, macOS, and Linux  

## 📦 Requirements

### Essential Dependencies
```bash
pip install opencv-python
```

### Enhanced Features (Recommended)
```bash
pip install pyzbar
```

### Complete Installation
```bash
pip install opencv-python pyzbar argparse pathlib
```

## 🚀 Quick Start

### Basic Usage (Webcam)
```bash
python qr_scanner.py
```

### Advanced Usage Examples

**Single Detection Mode:**
```bash
python qr_scanner.py --single
```

**With Logging:**
```bash
python qr_scanner.py --log
```

**External Camera:**
```bash
python qr_scanner.py --source 1
```

**RTSP Stream (Drone):**
```bash
python qr_scanner.py --source "rtsp://192.168.1.100:8080/live"
```

**HTTP Stream:**
```bash
python qr_scanner.py --source "http://drone_ip:8080/stream"
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` or `ESC` | Quit application |
| `s` | Save current frame |
| `p` | Pause/Resume scanning |

## 🛠️ Command Line Options

```bash
usage: qr_scanner.py [-h] [--source SOURCE] [--continuous] [--single] [--log] [--no-display]

Enhanced QR Code Scanner

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE, -s SOURCE
                        Video source (0 for webcam, URL for streams)
  --continuous, -c      Continue scanning after first detection (default)
  --single              Exit after first QR code detection
  --log, -l             Save detected QR codes to log file
  --no-display         Don't display QR text on video frame
```

## 🚁 Drone Integration

### Supported Drone Platforms

**DJI Drones:**
```bash
# Standard DJI stream
python qr_scanner.py --source "rtmp://192.168.1.1:1935/live"

# DJI Mobile SDK stream
python qr_scanner.py --source "rtsp://192.168.1.1:8080/live"
```

**Custom Drones:**
```bash
# Generic RTSP stream
python qr_scanner.py --source "rtsp://drone_ip:554/stream"

# UDP stream
python qr_scanner.py --source "udp://drone_ip:1234"
```

**ArduPilot/PX4:**
```bash
# MAVLink video stream
python qr_scanner.py --source "udp://127.0.0.1:5600"
```

### Drone Configuration Examples

**For FPV Racing Drones:**
```python
# Low latency configuration
python qr_scanner.py --source "udp://192.168.1.10:5600" --single
```

**For Survey/Mapping Applications:**
```python
# Continuous logging for waypoint navigation
python qr_scanner.py --source "rtsp://drone:8080/hd" --log --continuous
```

## 🏗️ Code Architecture

### Class Structure
```
QRCodeScanner
├── __init__()          # Initialize scanner with configuration
├── detect_qr_pyzbar()  # Enhanced QR detection using pyzbar
├── detect_qr_opencv()  # Built-in OpenCV QR detection
├── draw_qr_detection() # Visual feedback rendering
├── log_qr_detection()  # Data logging functionality
├── run()               # Main scanning loop
└── cleanup()           # Resource cleanup
```

### Detection Flow
1. **Video Capture**: Initialize video stream from source
2. **Frame Processing**: Continuous frame capture and processing
3. **Dual Detection**: Try pyzbar first, fallback to OpenCV
4. **Visual Feedback**: Draw bounding boxes and display data
5. **Data Handling**: Print to console and optionally log to file
6. **Mode Control**: Handle single vs continuous operation

## 📊 Output Examples

### Console Output
```
✅ Pyzbar available - Enhanced QR detection enabled
🎥 Video capture initialized successfully
🚀 QR Code Scanner started!
🎯 QR Code detected (pyzbar): https://example.com/qr-data
📝 Logged to qr_scan_log.txt
💾 Frame saved as qr_scan_20250613_143022.jpg
```

### Log File Format
```
2025-06-13 14:30:22 | pyzbar | https://example.com/qr-data
2025-06-13 14:31:15 | opencv | QR_CODE_TEXT_DATA_HERE
2025-06-13 14:32:08 | pyzbar | {"type":"json","data":"example"}
```

## 🔧 Performance Optimization

### For Resource-Constrained Systems
```python
# Modify these settings in the code:
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
self.cap.set(cv2.CAP_PROP_FPS, 15)
```

### For High-Resolution Applications
```python
# For 4K drone feeds:
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
self.cap.set(cv2.CAP_PROP_FPS, 30)
```

## 🐛 Troubleshooting

### Common Issues and Solutions

**"Failed to open video source"**
- ✅ Check camera connection and permissions
- ✅ Try different source indices (0, 1, 2)
- ✅ Verify RTSP/HTTP URLs are accessible
- ✅ Ensure camera isn't used by another app

**Poor QR Detection Performance**
- ✅ Improve lighting conditions
- ✅ Ensure QR codes are properly sized (not too small/large)
- ✅ Clean camera lens
- ✅ Reduce camera movement/vibration
- ✅ Try both detection methods

**Drone Connection Issues**
- ✅ Verify network connectivity to drone
- ✅ Check drone's video streaming settings
- ✅ Confirm RTSP/UDP port configuration
- ✅ Test stream URL in VLC or similar player first

**High CPU Usage**
- ✅ Reduce frame resolution
- ✅ Lower frame rate
- ✅ Use single detection method only
- ✅ Disable on-screen display with `--no-display`

### Debug Mode
Add this to enable verbose debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔄 Advanced Features

### Multiple QR Code Detection
The scanner automatically handles multiple QR codes in a single frame when using pyzbar.

### Custom Detection Areas
Modify the code to scan only specific regions:
```python
# Add region of interest (ROI) processing
roi = frame[y1:y2, x1:x2]
qr_results = self.detect_qr_pyzbar(roi)
```

### Integration with Drone SDKs

**DJI Tello:**
```python
from djitellopy import Tello
# Initialize Tello and get video stream
# Then use stream URL with scanner
```

**ArduPilot/MAVLink:**
```python
from pymavlink import mavutil
# Connect to flight controller
# Process video stream through scanner
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
git clone <repository-url>
cd qr-scanner
pip install -r requirements.txt
python -m pytest tests/  # Run tests
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- **OpenCV Community** for computer vision tools
- **Pyzbar Developers** for enhanced QR code detection
- **Drone Development Communities** for integration insights
- **Original Authors**: 
  - [Amit Kumar](https://github.com/1Amitkry) - Initial QR scanner concept
  - [Saurav Bhowmick](https://github.com/SauravBhowmick) - Drone integration approach

## 📞 Support

For support, questions, or feature requests:
- 🐛 **Issues**: Open an issue on GitHub
- 📧 **Email**: Contact maintainers
- 📖 **Documentation**: Check this README and code comments

---

## 🚀 Future Enhancements

### Planned Features
- 🔊 **Audio Feedback**: Sound alerts for QR detection
- 📱 **Mobile App**: Companion mobile application
- 🌐 **Web Interface**: Browser-based control panel
- 🤖 **AI Integration**: Machine learning for improved detection
- 📊 **Analytics Dashboard**: Detection statistics and reporting
- 🔐 **Security Features**: Encrypted QR code handling
- 🗺️ **GPS Integration**: Location tagging for drone applications

### API Development
- REST API for remote control
- WebSocket support for real-time data
- Integration with popular drone management platforms

---

**⚠️ Note**: This application is designed for educational and development purposes. Ensure compliance with local regulations when using drones and camera systems. Always test thoroughly in controlled environments before deployment.